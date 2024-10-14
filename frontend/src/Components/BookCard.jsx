// src/BookCard.jsx
import React, { useState } from 'react'; 
import { toast } from 'react-toastify'; 
import { axiosInstance } from '../utils/axiosInstance'; 

const BookCard = ({ book , borrowed ,available }) => {
    const [localStatus, setLocalStatus] = useState(book.status); 

    const borrowBook = async () => {
        const userId = localStorage.getItem('user_id');
        const bookId = book.id; 

        if (!userId) {
            toast.error("User ID not found. Please log in.");
            return;
        }
        setLocalStatus('borrowed');
        
        try {
            const response = await axiosInstance.post('/borrow_book', {
                user_id: userId,
                book_id: bookId,
            });
            toast.success(response.data.message); 
        } catch (error) {
            console.error('Error borrowing book:', error);
            const errorMessage = error.response?.data?.error || "An error occurred while borrowing the book.";
            toast.error(errorMessage); 
            setLocalStatus(book.status);
        }
    };

    const returnBook = async () => {
        const userId = localStorage.getItem('user_id');
        const bookId = book.id; 

        if (!userId) {
            toast.error("User ID not found. Please log in.");
            return;
        }

        setLocalStatus('available');

        try {
            const response = await axiosInstance.post('/return_book', {
                user_id: userId,
                book_id: bookId,
            });

            toast.success(response.data.message); 
        } catch (error) {
            console.error('Error returning book:', error);
            const errorMessage = error.response?.data?.error || "An error occurred while returning the book.";
            toast.error(errorMessage); 
            setLocalStatus(book.status);
        }
    };

    return (
        <div className="  bg-gray-800 p-4 h-[380px] overflow-hidden rounded shadow-md m-2 w-72  flex flex-col  opacity-95 hover:opacity-100 justify-between">
          <div>
          <img 
                src={book.image} 
                alt={book.title} 
                className="h-40 w-full object-contain rounded"
            />
            <h3 className="text-xl font-semibold mt-2 text-white truncate">{book.title}</h3>
            <h4 className="text-md text-gray-300 truncate">{book.subtitle}</h4>
            <p className="text-gray-400 mt-1">Authors: <span className="text-blue-400">{book.authors.split(',').slice(0, 3).join(', ')}</span></p>
            <p className="text-gray-400">Status: <span className="text-green-400">{localStatus}</span></p>
          </div>
            <div>
            {
                 localStatus === 'available' ? (
                    <button
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
                        onClick={borrowBook}
                    >
                        Borrow
                    </button>
                ) : null
            } 
             {
               available && localStatus === 'borrowed' ? (
                    <p
                        className=" text-red-500 font-bold text-xl mt-4"
                    >
                     Unavailable 
                    </p>
                ) : null
            }
            {
                borrowed ? (
                    <button
                        className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mt-4"
                        onClick={returnBook}
                    >
                        Return
                    </button>
                ) : null
            }
            </div>
        </div>
    );
};

export default BookCard;

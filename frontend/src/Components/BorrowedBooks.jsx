import React, { useEffect, useState } from 'react';
import BookCard from './BookCard';
import { axiosInstance } from '../utils/axiosInstance';

const BorrowedBooks = () => {
    const [borrowedBooks, setBorrowedBooks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    const userId = localStorage.getItem('user_id') || '1';


    const fetchBorrowedBooks = async () => {
        try {
            const response = await axiosInstance.get(`/my_borrowed_books?user_id=${userId}`);
            setBorrowedBooks(response.data);
            console.log(response.data)
        } catch (err) {
            setError(err.response?.data?.error || 'Something went wrong!');
        } finally {
            setLoading(false);
        }
    };


    useEffect(() => {
       
        fetchBorrowedBooks();
    }, [userId]);

    if (loading) return <p>Loading borrowed books...</p>;
    if (error) return <p>Error: {error}</p>;

    return (
        <div className=" flex h-[90vh]  flex-wrap justify-center  gap-4   ">
            {borrowedBooks.length > 0 ? (
                borrowedBooks.map(book => (
                    <BookCard key={book.id} book={{ ...book, status: 'borrowed' }} borrowed={true}  />

                ))
            ) : (
                <p>No borrowed books found.</p>
            )}
        </div>
    );
};

export default BorrowedBooks;

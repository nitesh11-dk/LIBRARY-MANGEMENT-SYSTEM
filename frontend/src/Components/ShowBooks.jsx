import { useEffect, useState } from 'react';
import BookCard from './BookCard.jsx';
import { axiosInstance } from '../utils/axiosInstance.jsx';
import { toast } from 'react-toastify';

const ShowBooks = () => {
    const [books, setBooks] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');

    const fetchBooks = async () => {
        try {
            const response = await axiosInstance.get('/all_books');
            setBooks(response.data);
        } catch (error) {
            console.error('Error fetching books:', error);
            toast.error('Failed to load books.');
        }
    };

    useEffect(() => {
        fetchBooks();
    }, []);


    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };


    const filteredBooks = books.filter(book =>
        book.title.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div className='flex flex-col items-center h-[90vh] bg-gray-900 overflow-auto'>
            <input
                type="text"
                placeholder="Search books..."
                value={searchTerm}
                onChange={handleSearchChange}
                className='mb-4 p-2 rounded outline-none text-black'
            />
            <div className='flex h-full w-full flex-wrap justify-center gap-4'>
                {filteredBooks.length > 0 ? (
                    filteredBooks.map(book => <BookCard key={book.id} book={book} available={true} />)
                ) : (
                    <h2 className="text-3xl font-semibold">No books available.</h2>
                )}
            </div>
        </div>
    );
};

export default ShowBooks;

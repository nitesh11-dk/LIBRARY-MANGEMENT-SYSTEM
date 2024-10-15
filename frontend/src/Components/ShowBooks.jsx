import { useEffect ,useState } from 'react';
import BookCard from './BookCard.jsx'; 
import { axiosInstance } from '../utils/axiosInstance.jsx';
import { toast } from 'react-toastify';

const ShowBooks = () => {
    const [books, setBooks] = useState([]);

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
  return (
       <div className='flex h-[90vh] bg-gray-900 overflow-auto  flex-wrap justify-center  gap-4  ' >
                    {books.length > 0 ? (
                        books.map(book => <BookCard key={book.id} book={book} available={true} />) 
                    ) : (
                        <h2 className="text-3xl font-semibold">No books available.</h2>
                    )}
                </div>
  )
}

export default ShowBooks

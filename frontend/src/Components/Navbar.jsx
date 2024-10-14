// src/Navbar.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="w-fit  items-center  flex  gap-4">
            <p>
                <Link 
                    to="/home/show_books" 
                    className="text-gray-300 hover:text-white transition-colors duration-200 text-lg font-semibold"
                >
                    📚 Show All Books
                </Link>
            </p>
            <p>
                <Link 
                    to="/home/borrowed_books" 
                    className="text-gray-300 hover:text-white transition-colors duration-200 text-lg font-semibold"
                >
                    📦 Borrowed Books
                </Link>
            </p>
        </nav>
    );
};

export default Navbar;

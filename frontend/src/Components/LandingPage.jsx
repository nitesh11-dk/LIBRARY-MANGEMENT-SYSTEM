import React from 'react';
import { Link } from 'react-router-dom';


const LandingPage = () => {
    return (
        <div className="min-h-screen flex flex-col bg-gray-900 text-gray-200">
            <header className="flex justify-between items-center p-4 shadow-md">
                <h1 className="text-2xl font-bold">Logo</h1>
                <div>
                    <Link to="/login" className="bg-blue-600 text-white px-4 py-2 rounded mr-2">
                        Login
                    </Link>
                    <Link to="/signup" className="bg-green-600 text-white px-4 py-2 rounded">
                        Signup
                    </Link>
                </div>
            </header>
            <main className="flex-grow flex flex-col items-center justify-center">
                <h1 className="text-5xl font-bold mb-4">Library Management System</h1>
                <h2 className="text-2xl font-semibold">
                    Welcome to Your Library
                </h2>
            </main>
            <footer className="p-4 text-center">
                <p>&copy; 2024 Your Library. All rights reserved.</p>
            </footer>
        </div>
    );
};

export default LandingPage;

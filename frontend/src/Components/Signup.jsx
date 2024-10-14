import React, { useState } from 'react';
import { axiosInstance } from '../utils/axiosInstance';
import { useNavigate, Link } from 'react-router-dom';
import { toast } from 'react-toastify';

const Signup = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault(); 
        try {
            const response = await axiosInstance.post('/create_user', {
                username,
                password,
            });
            toast.success(response.data.message); 
            navigate('/login');
        } catch (error) {
            if (error.response) {
                toast.error(error.response.data.error); 
            } else {
                toast.error('An unexpected error occurred.');
            }
        }
    };

    return (
        <div className="min-h-screen flex flex-col bg-gray-900 text-gray-200 n">
            <main className="flex-grow flex items-center justify-center">
                <form onSubmit={handleSubmit} className="bg-gray-800 p-6 rounded-xl shadow-md">
                    <h2 className="text-3xl overflow-hidden font-semibold mb-4">Sign Up</h2>
                    <div className="mb-4">
                        <label className="block text-sm mb-1">Username:</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            className="w-full p-2 rounded bg-gray-700 text-gray-200"
                            required
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-sm mb-1">Password:</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full p-2 rounded bg-gray-700 text-gray-200"
                            required
                        />
                    </div>
                    <div className='flex w-full gap-4'>
                        <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded">
                            Sign Up
                        </button>
                    </div>
                    <p className="mt-4 text-center">
                        Already have an account? 
                        <Link to={"/login"} className="text-blue-500 hover:underline ml-1">
                            Login
                        </Link>
                    </p>
                </form>
            </main>
        </div>
    );
};

export default Signup;

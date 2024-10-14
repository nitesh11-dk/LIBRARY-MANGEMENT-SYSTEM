import React from 'react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Outlet } from 'react-router-dom';
import Navbar from './Navbar';
const Home = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('username'); 
        localStorage.removeItem('user_id'); 
        toast.success('Successfully logged out!'); 
        navigate('/login'); 
    };


    const username = localStorage.getItem('username');

    return (
       
        <div className="h-screen  w-screen flex flex-col bg-gray-900 text-gray-200 overflow-hidden ">
                   
                   <nav className='flex justify-between items-center px-16 py-4 mb-1 shadow-md overflow-hidden  bg-gray-900'>
             {username && <span className="mr-4 text-xl font-bold">👧🏻 {username}!</span>}
                 <Navbar></Navbar>

               
                    <button
                        onClick={handleLogout}
                        className="bg-red-600 text-white px-4 py-2 rounded"
                    >
                        Logout
                    </button>
        </nav>
<p    className=" text-gray-300 hover:text-white transition-colors duration-200 text-2xl font-semibold mx-auto mb-4 overflow-hidden"> All Books </p>
           <Outlet/>
        </div>
    );
};

export default Home;

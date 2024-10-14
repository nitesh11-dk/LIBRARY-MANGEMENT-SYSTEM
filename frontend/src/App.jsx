import React from 'react';
import { Route , Routes } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import ShowBooks from './Components/ShowBooks.jsx';
import LandingPage from './Components/LandingPage';
import Signup from './Components/Signup';
import Login from './Components/Login';
import Home from './Components/Home';
import BorrowedBooks from './Components/ BorrowedBooks.jsx';

function App() {
  return (
    <>
    <div className='h-screen w-screen'>
     <ToastContainer position='bottom-right'/>

     <Routes>
      <Route path='/lp' element = {<LandingPage />} > </Route>
      <Route path='/signup' element = {<Signup />} > </Route>
      <Route path='/login' element = {<Login />} > </Route>
      <Route path='/home' element = {<Home />} > 
      
      <Route path='/home/borrowed_books' element = {<BorrowedBooks />} > </Route>
      <Route path='/home/show_books' element = {<ShowBooks />} > </Route>

      </Route>
     </Routes>
    </div>
    </>
  );
}

export default App;

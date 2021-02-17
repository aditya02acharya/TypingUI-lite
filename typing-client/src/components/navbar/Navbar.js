import React from 'react';
import logo from './../../images/logo.png'

const Navbar = () => {
  return (
    <nav className='flex justify-between items-center h-16 bg-gray-50 text-black relative shadow-md font-mono' role="navigation">
      <div className='pl-56'>
        <img src={logo} alt='Logo' width="200" height="50"/>
      </div>
      <div className='pr-56 flex flex-row-reverse'>
        <div className='p-4'>
          <a href="https://userinterfaces.aalto.fi/touchscreen-typing/">Project</a>
        </div>
        <div className='p-4'>
          <a href="https://userinterfaces.aalto.fi/">Group</a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

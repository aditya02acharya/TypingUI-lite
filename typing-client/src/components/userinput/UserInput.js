import React from 'react';

const UserInput = (props) => {
  return (
    <div className="bg-gray-50 flex flex-col justify-left items-center w-1/2 h-screen shadow-lg">
      <div className="w-1/2 text-left pt-36">
        <h1 className="text-4xl font-bold font-sans text-black-500 mb-2">Ai Typist</h1>
        <p className= "text-gray-500 pt-4">
        Enter a sentence below for the model to generate a simulation video.
        Limit the sentence length to 15 characters, english alphabets and without
        any special characters.
        </p>
      </div>
      <div className="w-1/2 text-left pt-12">
        <input type="text" name="hello" placeholder="hello" autocomplete="off"
        maxlength="15" className="shadow-md border w-full h-10 px-3 py-2 text-orange-500 focus:outline-none focus:border-orange-500 mb-3 rounded"/>
        <button className="bg-purple-600 hover:bg-purple-500 text-white px-6 py-1 rounded text-lg focus:outline-none shadow">Type</button>
      </div>
    </div>
  );
};

export default UserInput;

"use client";

import {Menu, Search} from "lucide-react";
import Link from "next/link";
import {FormEvent, useRef} from "react";

const TopNavigation = () => {
        const searchInputRef = useRef<HTMLInputElement>(null);

        const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
            event.preventDefault();

            if (searchInputRef.current) {
                console.log(searchInputRef.current.value);
            }
        };
        
    return (
        <nav className='fixed top-0 left-0 w-screen z-20 dark:bg-black bg-white'>
            <div className='flex justify-between items-center px-2 md:px-7 h-16'>
                {/* Top Icon and Name with Drop Down Menu */}
                <div className="flex items-center">
                    <span className="hover:bg-background-dark/30 md:block hidden hover:text-white cursor-pointer rounded-full p-2 mr-1">
                        <Menu size={30}/>
                    </span>
                    <Link href="/" className="flex items-center space-x-2">
                        <svg 
                            role="img" 
                            viewBox="0 0 24 24" 
                            xmlns="http://www.w3.org/2000/svg"
                        >   
                            <title>YouTube</title>
                            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                        </svg>                
                        <span className='hidden md:block text-2xl font-bold'>ViTube</span>
                    </Link>
                </div>

                {/* Search Bar */}
                <div className='md:flex items-center justify-center hidden'>
                    <form 
                    onSubmit={handleSubmit} 
                    className="flex items-center h-10 mx-auto"
                    >
                        <input 
                            type='search' 
                            placeholder='Search' 
                            ref={searchInputRef} 
                            className="px-4 h-full md:w-48 lg:w-96 border dark:border-gray-50 border-gray-300 rounded-l-full focus:outline-none" 
                        />
                        <div className="h-full px-5 grid place-content-center bg-background-light text-black rounded-r-full">
                            <Search />
                        </div>
                    </form>
                </div>
            </div>
        </nav>
    );
};

export default TopNavigation;
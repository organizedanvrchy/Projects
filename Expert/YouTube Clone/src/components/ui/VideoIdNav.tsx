"use client";

import AppContext from "@/context/appContext";
import { useContext } from "react";
import Sidebar from "./Sidebar";
import { cn } from "@/lib/utils";

const VideoIdNav = () => {
    const {showNav, setShowNav} = useContext(AppContext)

    return (
        <>
            {showNav && (
                <div 
                    onClick={() => setShowNav(prevState => !prevState)} 
                    className="w-screen h-screen top-0 left-0 z-30 fixed bg-[rgba(0, 0, 0, 0,75)]" 
                /> 
            )}
            <Sidebar className={cn(showNav ? "translate-x-0" : "")} />
        </>
    );
};

export default VideoIdNav;
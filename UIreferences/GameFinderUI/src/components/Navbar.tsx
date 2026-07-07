import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Gamepad2, Moon, Sun } from 'lucide-react';
interface NavbarProps {
  isDark: boolean;
  toggleTheme: () => void;
}
export function Navbar({ isDark, toggleTheme }: NavbarProps) {
  const location = useLocation();
  const navLinks = [
  {
    name: 'Home',
    path: '/'
  },
  {
    name: 'Recommendation',
    path: '/recommendation'
  },
  {
    name: 'About',
    path: '/about'
  }];

  return (
    <nav className="sticky top-0 z-50 w-full border-b border-slate-200 dark:border-slate-800/50 bg-white/80 dark:bg-[#0a0e1a]/80 backdrop-blur-md transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        {/* Logo */}
        <Link to="/" className="flex items-center gap-2 group">
          <div className="p-2 bg-blue-100 dark:bg-blue-500/10 rounded-lg group-hover:bg-blue-200 dark:group-hover:bg-blue-500/20 transition-colors">
            <Gamepad2 className="w-6 h-6 text-blue-600 dark:text-blue-500" />
          </div>
          <span className="text-xl font-bold text-slate-900 dark:text-white tracking-tight">
            GameFinder
          </span>
        </Link>

        {/* Links */}
        <div className="hidden md:flex items-center gap-8">
          {navLinks.map((link) => {
            const isActive =
            location.pathname === link.path ||
            link.path !== '/' && location.pathname.startsWith(link.path);
            return (
              <Link
                key={link.name}
                to={link.path}
                className={`text-sm font-medium transition-colors relative py-2 ${isActive ? 'text-slate-900 dark:text-white' : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'}`}>
                
                {link.name}
                {isActive &&
                <span className="absolute bottom-0 left-0 w-full h-0.5 bg-blue-600 dark:bg-blue-500 rounded-t-full" />
                }
              </Link>);

          })}
        </div>

        {/* Theme Toggle */}
        <button
          onClick={toggleTheme}
          className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 dark:bg-slate-800/50 border border-slate-200 dark:border-slate-700/50 hover:bg-slate-200 dark:hover:bg-slate-800 transition-colors text-sm font-medium text-slate-700 dark:text-slate-300">
          
          {isDark ?
          <>
              <Moon className="w-4 h-4" />
              <span>Dark</span>
            </> :

          <>
              <Sun className="w-4 h-4 text-amber-500" />
              <span>Light</span>
            </>
          }
        </button>
      </div>
    </nav>);

}
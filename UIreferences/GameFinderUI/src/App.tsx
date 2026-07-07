import React, { useEffect, useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Home } from './pages/Home';
import { Recommendation } from './pages/Recommendation';
import { Results } from './pages/Results';
import { GameDetail } from './pages/GameDetail';
export function App() {
  const [isDark, setIsDark] = useState(true);
  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDark]);
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-slate-50 dark:bg-[#0a0e1a] text-slate-900 dark:text-slate-200 font-sans selection:bg-blue-500/30 transition-colors duration-200">
        <Navbar isDark={isDark} toggleTheme={() => setIsDark(!isDark)} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/recommendation" element={<Recommendation />} />
          <Route path="/results" element={<Results />} />
          <Route path="/game/:id" element={<GameDetail />} />
        </Routes>
      </div>
    </BrowserRouter>);

}
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, Laptop, Monitor, MonitorUp, Star, Clock } from 'lucide-react';
import { useScreenInit } from '../useScreenInit';
const GENRES = [
'Action',
'Adventure',
'RPG',
'Strategy',
'Simulation',
'Indie',
'Racing',
'Sports',
'Horror',
'+ More'];

export function Recommendation() {
  useScreenInit();
  const navigate = useNavigate();
  const [budget, setBudget] = useState(300000);
  const [selectedGenre, setSelectedGenre] = useState('Action');
  const [pcLevel, setPcLevel] = useState(2);
  const [rating, setRating] = useState(75);
  const [playtime, setPlaytime] = useState('Medium');
  const handleSearch = () => {
    navigate('/results');
  };
  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#0a0e1a] py-12 transition-colors duration-200">
      <div className="max-w-3xl mx-auto px-6">
        <div className="text-center mb-10">
          <h1 className="text-4xl font-bold text-slate-900 dark:text-white mb-4">
            Find Your Perfect Game
          </h1>
          <p className="text-slate-600 dark:text-slate-400">
            Tell us your preferences and let our AI find the best games for you
          </p>
        </div>

        <div className="glass-card p-8 space-y-10">
          {/* 1. Budget Range */}
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-slate-900 dark:text-white">
                1. Budget Range
              </h3>
              <span className="text-blue-600 dark:text-blue-400 font-medium">
                Rp {budget.toLocaleString('id-ID')}
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="10000000"
              step="50000"
              value={budget}
              onChange={(e) => setBudget(Number(e.target.value))}
              className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-lg appearance-none cursor-pointer accent-blue-600 dark:accent-blue-500" />
            
            <div className="flex justify-between text-xs text-slate-500">
              <span>Rp 0</span>
              <span>Rp 10.000.000</span>
            </div>
          </div>

          {/* 2. Genre */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold text-slate-900 dark:text-white">
              2. Genre
            </h3>
            <div className="relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400 dark:text-slate-500" />
              <input
                type="text"
                placeholder="Search or select genre..."
                className="w-full bg-white dark:bg-[#0f1626] border border-slate-200 dark:border-slate-800 rounded-lg py-2.5 pl-10 pr-4 text-sm text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-blue-500 transition-colors" />
              
            </div>
            <div className="flex flex-wrap gap-2 pt-2">
              {GENRES.map((genre) =>
              <button
                key={genre}
                onClick={() => setSelectedGenre(genre)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-colors border ${selectedGenre === genre ? 'bg-blue-50 dark:bg-blue-500/20 border-blue-600 dark:border-blue-500 text-blue-600 dark:text-blue-400' : 'bg-white dark:bg-[#0f1626] border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:border-slate-300 dark:hover:border-slate-600'}`}>
                
                  {genre}
                </button>
              )}
            </div>
          </div>

          {/* 3. PC Level */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold text-slate-900 dark:text-white">
              3. PC Level
            </h3>
            <div className="grid grid-cols-3 gap-4">
              {[
              {
                id: 1,
                name: 'Low End',
                desc: '(Level 1)',
                icon: Laptop
              },
              {
                id: 2,
                name: 'Mid End',
                desc: '(Level 2)',
                icon: Monitor
              },
              {
                id: 3,
                name: 'High End',
                desc: '(Level 3)',
                icon: MonitorUp
              }].
              map((level) => {
                const Icon = level.icon;
                const isSelected = pcLevel === level.id;
                return (
                  <button
                    key={level.id}
                    onClick={() => setPcLevel(level.id)}
                    className={`flex flex-col items-center justify-center p-6 rounded-xl border transition-all ${isSelected ? 'bg-blue-50 dark:bg-blue-500/10 border-blue-600 dark:border-blue-500' : 'bg-white dark:bg-[#0f1626] border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'}`}>
                    
                    <Icon
                      className={`w-8 h-8 mb-3 ${isSelected ? 'text-blue-600 dark:text-blue-400' : 'text-slate-400 dark:text-slate-500'}`} />
                    
                    <span
                      className={`text-sm font-medium ${isSelected ? 'text-blue-600 dark:text-blue-400' : 'text-slate-700 dark:text-slate-300'}`}>
                      
                      {level.name}
                    </span>
                    <span className="text-xs text-slate-500 mt-1">
                      {level.desc}
                    </span>
                  </button>);

              })}
            </div>
          </div>

          {/* 4. Preferred Rating */}
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <h3 className="text-lg font-semibold text-slate-900 dark:text-white">
                4. Preferred Rating
              </h3>
              <div className="flex items-center gap-1">
                {[1, 2, 3, 4].map((i) =>
                <Star
                  key={i}
                  className={`w-5 h-5 ${i <= 3 ? 'text-yellow-400 dark:text-yellow-500 fill-yellow-400 dark:fill-yellow-500' : 'text-yellow-400/50 dark:text-yellow-500/50 fill-yellow-400/50 dark:fill-yellow-500/50'}`} />

                )}
                <Star className="w-5 h-5 text-slate-200 dark:text-slate-700 fill-slate-200 dark:fill-slate-700" />
              </div>
              <span className="text-slate-600 dark:text-slate-400 text-sm">
                ({rating}%)
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="100"
              value={rating}
              onChange={(e) => setRating(Number(e.target.value))}
              className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-lg appearance-none cursor-pointer accent-blue-600 dark:accent-blue-500" />
            
            <div className="flex justify-between text-xs text-slate-500">
              <span>0%</span>
              <span>100%</span>
            </div>
          </div>

          {/* 5. Preferred Playtime */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold text-slate-900 dark:text-white">
              5. Preferred Playtime
            </h3>
            <div className="grid grid-cols-3 gap-4">
              {[
              {
                id: 'Short',
                name: 'Short',
                desc: '(< 10 hours)'
              },
              {
                id: 'Medium',
                name: 'Medium',
                desc: '(10 - 50 hours)'
              },
              {
                id: 'Long',
                name: 'Long',
                desc: '(> 50 hours)'
              }].
              map((time) => {
                const isSelected = playtime === time.id;
                return (
                  <button
                    key={time.id}
                    onClick={() => setPlaytime(time.id)}
                    className={`flex flex-col items-center justify-center p-4 rounded-xl border transition-all ${isSelected ? 'bg-blue-50 dark:bg-blue-500/10 border-blue-600 dark:border-blue-500' : 'bg-white dark:bg-[#0f1626] border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'}`}>
                    
                    <span
                      className={`text-sm font-medium ${isSelected ? 'text-blue-600 dark:text-blue-400' : 'text-slate-700 dark:text-slate-300'}`}>
                      
                      {time.name}
                    </span>
                    <span className="text-xs text-slate-500 mt-1">
                      {time.desc}
                    </span>
                  </button>);

              })}
            </div>
            <div className="pt-4 relative">
              <div className="absolute top-6 left-0 w-full h-1 bg-slate-200 dark:bg-slate-800 rounded-full" />
              <div className="absolute top-6 left-0 w-1/2 h-1 bg-blue-600 dark:bg-blue-500 rounded-full" />
              <div className="flex justify-between text-xs text-slate-500 mt-8">
                <span>0h</span>
                <span>25h</span>
                <span>50h</span>
                <span>100h+</span>
              </div>
            </div>
          </div>

          <button
            onClick={handleSearch}
            className="w-full gradient-btn py-4 text-lg flex items-center justify-center gap-2 mt-8">
            
            <Search className="w-5 h-5" />
            Find My Game
          </button>
        </div>
      </div>
    </div>);

}
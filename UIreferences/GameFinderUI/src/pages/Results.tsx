import React from 'react';
import { Link } from 'react-router-dom';
import { Heart, ChevronDown } from 'lucide-react';
import { useScreenInit } from '../useScreenInit';
const RESULTS = [
{
  id: 1,
  title: 'Zombie Panic Source',
  tags: ['Action', 'FPS', 'Zombies'],
  score: 90.03,
  rating: 85.71,
  hours: 208.5,
  price: 'Rp 0',
  free: true,
  image:
  'https://images.unsplash.com/photo-1505775561242-727b7fba578e?auto=format&fit=crop&w=100&q=80'
},
{
  id: 2,
  title: 'Pirates Vikings & Knights II',
  tags: ['Action', 'Adventure', 'RPG'],
  score: 90.03,
  rating: 85.23,
  hours: 98.3,
  price: 'Rp 0',
  free: true,
  image:
  'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=100&q=80'
},
{
  id: 3,
  title: 'Command & Conquer 3 Tiberium Wars',
  tags: ['Strategy', 'RTS', 'Sci-fi'],
  score: 90.03,
  rating: 88.52,
  hours: 95.1,
  price: 'Rp 0',
  free: true,
  image:
  'https://images.unsplash.com/photo-1614294149010-950b698f72c0?auto=format&fit=crop&w=100&q=80'
},
{
  id: 4,
  title: 'Hitogata Happa',
  tags: ['Action', 'Indie'],
  score: 90.03,
  rating: 100.0,
  hours: 0.2,
  price: 'Rp 0',
  free: true,
  image:
  'https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=100&q=80'
},
{
  id: 5,
  title: 'Kingdoms of Amalur: Reckoning',
  tags: ['RPG', 'Action', 'Fantasy'],
  score: 90.03,
  rating: 100.0,
  hours: 74.4,
  price: 'Rp 0',
  free: true,
  image:
  'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=100&q=80'
},
{
  id: 6,
  title: 'Left 4 Dead 2',
  tags: ['Action', 'FPS', 'Zombies'],
  score: 89.12,
  rating: 96.76,
  hours: 671.2,
  price: 'Rp 0',
  free: true,
  image:
  'https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=100&q=80'
}];

export function Results() {
  useScreenInit();
  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#0a0e1a] py-12 transition-colors duration-200">
      <div className="max-w-5xl mx-auto px-6">
        <div className="flex items-end justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-slate-900 dark:text-white mb-2">
              Top 10 Recommendations
            </h1>
            <p className="text-slate-600 dark:text-slate-400">
              Based on your preferences
            </p>
          </div>
          <Link
            to="/recommendation"
            className="px-6 py-2.5 text-sm rounded-lg border border-blue-200 dark:border-blue-500/30 text-blue-600 dark:text-blue-400 font-medium hover:bg-blue-50 dark:hover:bg-blue-500/10 transition-colors">
            
            Modify Search
          </Link>
        </div>

        {/* Filters Summary */}
        <div className="glass-card p-4 mb-8 flex flex-wrap items-center gap-6 text-sm">
          <div>
            <span className="text-slate-500 block mb-1">Budget</span>
            <span className="text-slate-900 dark:text-slate-300 font-medium">
              Rp 300.000
            </span>
          </div>
          <div>
            <span className="text-slate-500 block mb-1">PC Level</span>
            <span className="text-slate-900 dark:text-slate-300 font-medium">
              Mid End (2)
            </span>
          </div>
          <div>
            <span className="text-slate-500 block mb-1">Rating</span>
            <span className="text-slate-900 dark:text-slate-300 font-medium">
              ≥ 75%
            </span>
          </div>
          <div>
            <span className="text-slate-500 block mb-1">Playtime</span>
            <span className="text-slate-900 dark:text-slate-300 font-medium">
              ≥ 20 hours
            </span>
          </div>
          <div>
            <span className="text-slate-500 block mb-1">Genre</span>
            <span className="text-slate-900 dark:text-slate-300 font-medium">
              Action
            </span>
          </div>
        </div>

        {/* List Header */}
        <div className="grid grid-cols-[auto_1fr_100px_100px_100px_auto] gap-4 px-6 py-3 border-b border-slate-200 dark:border-slate-800 text-xs font-medium text-slate-500 mb-4">
          <div className="w-8 text-center">#</div>
          <div>Game</div>
          <div className="flex items-center gap-1 cursor-pointer hover:text-slate-700 dark:hover:text-slate-300 text-blue-600 dark:text-blue-400">
            Score <ChevronDown className="w-3 h-3" />
          </div>
          <div className="flex items-center gap-1 cursor-pointer hover:text-slate-700 dark:hover:text-slate-300">
            Rating
          </div>
          <div className="flex items-center gap-1 cursor-pointer hover:text-slate-700 dark:hover:text-slate-300">
            Playtime
          </div>
          <div className="flex items-center gap-1 cursor-pointer hover:text-slate-700 dark:hover:text-slate-300">
            Price
          </div>
        </div>

        {/* Results List */}
        <div className="space-y-3">
          {RESULTS.map((game, index) =>
          <Link key={game.id} to={`/game/${game.id}`} className="block">
              <div className="glass-card p-4 flex items-center gap-6 hover:border-slate-300 dark:hover:border-slate-600 transition-colors group">
                {/* Rank */}
                <div
                className={`w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm border-2 ${index < 3 ? 'border-yellow-400 dark:border-yellow-500 text-yellow-500 dark:text-yellow-500 bg-yellow-50 dark:bg-transparent' : 'border-slate-200 dark:border-slate-700 text-slate-500 dark:text-slate-400 bg-slate-50 dark:bg-transparent'}`}>
                
                  {index + 1}
                </div>

                {/* Game Info */}
                <div className="flex items-center gap-4 flex-1">
                  <img
                  src={game.image}
                  alt={game.title}
                  className="w-24 h-14 object-cover rounded border border-slate-200 dark:border-slate-800" />
                
                  <div>
                    <h3 className="text-slate-900 dark:text-white font-medium mb-1.5 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                      {game.title}
                    </h3>
                    <div className="flex gap-2">
                      {game.tags.map((tag) =>
                    <span
                      key={tag}
                      className="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">
                      
                          {tag}
                        </span>
                    )}
                    </div>
                  </div>
                </div>

                {/* Score */}
                <div className="w-[100px]">
                  <div className="text-blue-600 dark:text-blue-400 font-semibold">
                    {game.score}
                  </div>
                  <div className="text-xs text-slate-500">Score</div>
                </div>

                {/* Rating */}
                <div className="w-[100px]">
                  <div className="text-slate-900 dark:text-slate-300 font-medium">
                    {game.rating}%
                  </div>
                </div>

                {/* Playtime */}
                <div className="w-[100px]">
                  <div className="text-slate-900 dark:text-slate-300 font-medium">
                    {game.hours}h
                  </div>
                </div>

                {/* Price */}
                <div className="w-[100px]">
                  <div className="text-slate-900 dark:text-slate-300 font-medium">
                    {game.price}
                  </div>
                  <div className="text-xs text-emerald-600 dark:text-emerald-500">
                    Free
                  </div>
                </div>

                {/* Action */}
                <button
                className="w-8 h-8 flex items-center justify-center rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-400 dark:text-slate-500 hover:text-red-500 dark:hover:text-red-400 transition-colors"
                onClick={(e) => e.preventDefault()}>
                
                  <Heart className="w-5 h-5" />
                </button>
              </div>
            </Link>
          )}
        </div>
      </div>
    </div>);

}
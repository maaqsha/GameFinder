import React from 'react';
import { Link } from 'react-router-dom';
import { Sparkles, Gamepad2, BrainCircuit, Star, Heart } from 'lucide-react';
import { useScreenInit } from '../useScreenInit';
const FEATURED_GAMES = [
{
  id: 1,
  title: 'Elden Ring',
  image:
  'https://images.unsplash.com/photo-1605901309584-818e25960b8f?auto=format&fit=crop&w=600&q=80',
  tags: ['RPG', 'Souls-like'],
  price: 'Rp 599.000',
  rating: 96
},
{
  id: 2,
  title: "Baldur's Gate 3",
  image:
  'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=600&q=80',
  tags: ['RPG', 'Strategy'],
  price: 'Rp 599.000',
  rating: 96
},
{
  id: 3,
  title: 'Hades',
  image:
  'https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=600&q=80',
  tags: ['Roguelike', 'Action'],
  price: 'Rp 118.999',
  rating: 97
},
{
  id: 4,
  title: 'Red Dead Redemption 2',
  image:
  'https://images.unsplash.com/photo-1486401899868-0e435ed85128?auto=format&fit=crop&w=600&q=80',
  tags: ['Adventure', 'Action'],
  price: 'Rp 299.000',
  rating: 98
},
{
  id: 5,
  title: 'Stardew Valley',
  image:
  'https://images.unsplash.com/photo-1592839719941-8e2651039d01?auto=format&fit=crop&w=600&q=80',
  tags: ['RPG', 'Simulation'],
  price: 'Rp 79.999',
  rating: 96
}];

export function Home() {
  useScreenInit();
  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#0a0e1a] pb-20 transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-6 pt-16">
        {/* Hero Section */}
        <div className="grid lg:grid-cols-2 gap-12 items-center mb-24">
          <div className="space-y-8">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-800/50 border border-slate-200 dark:border-slate-700/50 text-xs font-medium text-slate-600 dark:text-slate-300 uppercase tracking-wider">
              <Sparkles className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400" />
              Steam Game Recommendation System
            </div>

            <h1 className="text-5xl lg:text-6xl font-bold leading-tight text-slate-900 dark:text-white">
              Find Your Next <br />
              Favorite{' '}
              <span className="text-blue-600 dark:text-blue-500">Game</span>
            </h1>

            <p className="text-lg text-slate-600 dark:text-slate-400 max-w-xl leading-relaxed">
              Smart recommendation powered by Fuzzy Mamdani algorithm. Discover
              games that match your budget, PC specs, rating preference,
              playtime, and favorite genres.
            </p>

            <div className="flex flex-wrap items-center gap-4">
              <Link
                to="/recommendation"
                className="gradient-btn px-8 py-3.5 text-base shadow-lg shadow-blue-500/25">
                
                Start Recommendation
              </Link>
              <button className="px-8 py-3.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors text-slate-900 dark:text-white font-medium flex items-center gap-2">
                <BrainCircuit className="w-5 h-5" />
                Learn More
              </button>
            </div>
          </div>

          <div className="relative">
            <div className="absolute -inset-4 bg-blue-500/10 dark:bg-blue-500/20 blur-3xl rounded-full opacity-50" />
            <img
              src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1000&q=80"
              alt="Gamer at desk"
              className="relative rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xl dark:shadow-2xl object-cover aspect-[4/3] w-full" />
            
          </div>
        </div>

        {/* Features */}
        <div className="grid md:grid-cols-3 gap-6 mb-24">
          <div className="glass-card p-6 flex flex-col gap-4">
            <div className="w-12 h-12 rounded-xl bg-blue-50 dark:bg-blue-500/10 flex items-center justify-center border border-blue-100 dark:border-blue-500/20">
              <Sparkles className="w-6 h-6 text-blue-600 dark:text-blue-400" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-slate-900 dark:text-white mb-2">
                Smart Algorithm
              </h3>
              <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                Fuzzy Mamdani algorithm analyzes multiple factors to find your
                perfect game
              </p>
            </div>
          </div>

          <div className="glass-card p-6 flex flex-col gap-4">
            <div className="w-12 h-12 rounded-xl bg-blue-50 dark:bg-purple-500/10 flex items-center justify-center border border-blue-100 dark:border-purple-500/20">
              <Gamepad2 className="w-6 h-6 text-blue-600 dark:text-purple-400" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-slate-900 dark:text-white mb-2">
                150,000+ Games
              </h3>
              <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                Huge database of Steam games with real-time data and insights
              </p>
            </div>
          </div>

          <div className="glass-card p-6 flex flex-col gap-4">
            <div className="w-12 h-12 rounded-xl bg-blue-50 dark:bg-emerald-500/10 flex items-center justify-center border border-blue-100 dark:border-emerald-500/20">
              <BrainCircuit className="w-6 h-6 text-blue-600 dark:text-emerald-400" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-slate-900 dark:text-white mb-2">
                Personalized for You
              </h3>
              <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                Advanced fuzzy logic system for personalized recommendations
              </p>
            </div>
          </div>
        </div>

        {/* Featured Games */}
        <div>
          <div className="flex items-center justify-between mb-8">
            <div className="flex items-center gap-3">
              <Star className="w-6 h-6 text-yellow-500 fill-yellow-500" />
              <h2 className="text-2xl font-bold text-slate-900 dark:text-white">
                Featured Games
              </h2>
            </div>
            <button className="px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors text-sm font-medium text-slate-900 dark:text-white">
              View All
            </button>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
            {FEATURED_GAMES.map((game) =>
            <div
              key={game.id}
              className="group glass-card overflow-hidden hover:border-slate-300 dark:hover:border-slate-600 transition-colors flex flex-col">
              
                <div className="relative aspect-[3/4] overflow-hidden">
                  <img
                  src={game.image}
                  alt={game.title}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                
                  <button className="absolute top-3 right-3 p-2 rounded-full bg-black/50 backdrop-blur-sm text-slate-300 hover:text-white hover:bg-black/70 transition-all">
                    <Heart className="w-4 h-4" />
                  </button>
                </div>
                <div className="p-4 flex flex-col flex-1">
                  <h3 className="font-semibold text-slate-900 dark:text-white mb-2 line-clamp-1">
                    {game.title}
                  </h3>
                  <div className="flex flex-wrap gap-1.5 mb-4">
                    {game.tags.map((tag) =>
                  <span
                    key={tag}
                    className="px-2 py-0.5 rounded text-[10px] font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    
                        {tag}
                      </span>
                  )}
                  </div>
                  <div className="mt-auto flex items-center justify-between">
                    <span className="text-emerald-600 dark:text-emerald-400 font-semibold text-sm">
                      {game.price}
                    </span>
                    <div className="flex items-center gap-1 text-yellow-500">
                      <Star className="w-3 h-3 fill-current" />
                      <span className="text-xs font-medium text-slate-700 dark:text-yellow-500">
                        {game.rating}%
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>);

}
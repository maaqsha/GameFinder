import React from 'react';
import { Link } from 'react-router-dom';
import {
  ArrowLeft,
  ExternalLink,
  Heart,
  CheckCircle2,
  Star,
  Clock,
  Monitor,
  Wallet,
  Gamepad2 } from
'lucide-react';
import { useScreenInit } from '../useScreenInit';
export function GameDetail() {
  useScreenInit();
  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#0a0e1a] py-8 transition-colors duration-200">
      <div className="max-w-5xl mx-auto px-6">
        <Link
          to="/results"
          className="inline-flex items-center gap-2 text-sm text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 mb-8 transition-colors">
          
          <ArrowLeft className="w-4 h-4" />
          Back to Results
        </Link>

        <div className="grid lg:grid-cols-[1fr_350px] gap-8 mb-8">
          {/* Main Info */}
          <div className="glass-card p-8">
            <h1 className="text-4xl font-bold text-slate-900 dark:text-white mb-6">
              Left 4 Dead 2
            </h1>

            <div className="aspect-video rounded-xl overflow-hidden border border-slate-200 dark:border-slate-800 mb-8">
              <img
                src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1200&q=80"
                alt="Left 4 Dead 2"
                className="w-full h-full object-cover" />
              
            </div>

            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-slate-900 dark:text-white">
                About This Game
              </h2>
              <p className="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">
                Left 4 Dead 2 is a 2009 first-person shooter game developed and
                published by Valve. It is a sequel to Left 4 Dead and sees four
                new survivors fight against the zombie horde, the Infected.
              </p>
              <button className="text-blue-600 dark:text-blue-400 text-sm hover:text-blue-700 dark:hover:text-blue-300 font-medium">
                Read More ▾
              </button>
            </div>

            <div className="flex gap-4 mt-8">
              <button className="flex-1 gradient-btn py-3.5 flex items-center justify-center gap-2">
                <ExternalLink className="w-5 h-5" />
                View on Steam
              </button>
              <button className="flex-1 px-6 py-3.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors text-slate-900 dark:text-white font-medium flex items-center justify-center gap-2">
                <Heart className="w-5 h-5" />
                Add to Wishlist
              </button>
            </div>
          </div>

          {/* Sidebar Stats */}
          <div className="space-y-6">
            <div className="glass-card p-6 text-center">
              <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-blue-50 dark:bg-blue-500/10 border border-blue-100 dark:border-blue-500/20 mb-4">
                <span className="text-2xl font-bold text-slate-900 dark:text-white">
                  89.12{' '}
                  <span className="text-sm text-slate-500 font-normal">
                    /100
                  </span>
                </span>
              </div>
              <h3 className="text-slate-900 dark:text-slate-300 font-medium mb-1">
                Recommendation Score
              </h3>
              <p className="text-emerald-600 dark:text-emerald-400 text-sm font-medium">
                Highly Recommended
              </p>
              <div className="w-full h-1.5 bg-slate-100 dark:bg-slate-800 rounded-full mt-4 overflow-hidden">
                <div
                  className="h-full bg-emerald-500 rounded-full"
                  style={{
                    width: '89%'
                  }} />
                
              </div>
            </div>

            <div className="glass-card p-6 space-y-4">
              <div className="grid grid-cols-[100px_1fr] gap-4 text-sm">
                <span className="text-slate-500">Genre</span>
                <span className="text-slate-900 dark:text-slate-300 font-medium">
                  Action, FPS, Zombies
                </span>
              </div>
              <div className="grid grid-cols-[100px_1fr] gap-4 text-sm">
                <span className="text-slate-500">Rating</span>
                <span className="text-slate-900 dark:text-slate-300 font-medium">
                  96.76% (Very Positive)
                </span>
              </div>
              <div className="grid grid-cols-[100px_1fr] gap-4 text-sm">
                <span className="text-slate-500">Price</span>
                <span className="text-slate-900 dark:text-slate-300 font-medium">
                  Rp 0 (Free)
                </span>
              </div>
              <div className="grid grid-cols-[100px_1fr] gap-4 text-sm">
                <span className="text-slate-500">PC Level</span>
                <span className="text-emerald-600 dark:text-emerald-400 font-medium">
                  Low End (1)
                </span>
              </div>
              <div className="grid grid-cols-[100px_1fr] gap-4 text-sm">
                <span className="text-slate-500">Playtime</span>
                <span className="text-slate-900 dark:text-slate-300 font-medium">
                  671.2 hours
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Why Recommended */}
        <div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white mb-2">
            Why This Game Was Recommended
          </h2>
          <p className="text-slate-600 dark:text-slate-400 mb-6">
            Based on your preferences
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
            <div className="glass-card p-6 flex flex-col">
              <div className="flex items-center gap-2 mb-3">
                <Wallet className="w-5 h-5 text-blue-600 dark:text-blue-400" />
                <h3 className="font-semibold text-slate-900 dark:text-white">
                  Budget Match
                </h3>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-400 mb-4 flex-1">
                This game is free (Rp 0) and well within your budget of Rp
                300.000.
              </p>
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/20 text-emerald-600 dark:text-emerald-400 text-xs font-medium w-fit">
                <CheckCircle2 className="w-3.5 h-3.5" /> Excellent Match
              </div>
            </div>

            <div className="glass-card p-6 flex flex-col">
              <div className="flex items-center gap-2 mb-3">
                <Monitor className="w-5 h-5 text-blue-600 dark:text-blue-400" />
                <h3 className="font-semibold text-slate-900 dark:text-white">
                  PC Compatibility
                </h3>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-400 mb-4 flex-1">
                Runs perfectly on your Mid End PC (Level 2).
              </p>
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/20 text-emerald-600 dark:text-emerald-400 text-xs font-medium w-fit">
                <CheckCircle2 className="w-3.5 h-3.5" /> Excellent Match
              </div>
            </div>

            <div className="glass-card p-6 flex flex-col">
              <div className="flex items-center gap-2 mb-3">
                <Star className="w-5 h-5 text-fuchsia-500 dark:text-blue-400" />
                <h3 className="font-semibold text-slate-900 dark:text-white">
                  Rating Match
                </h3>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-400 mb-4 flex-1">
                96.76% rating is higher than your preferred 75%.
              </p>
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/20 text-emerald-600 dark:text-emerald-400 text-xs font-medium w-fit">
                <CheckCircle2 className="w-3.5 h-3.5" /> Excellent Match
              </div>
            </div>

            <div className="glass-card p-6 flex flex-col">
              <div className="flex items-center gap-2 mb-3">
                <Clock className="w-5 h-5 text-yellow-500" />
                <h3 className="font-semibold text-slate-900 dark:text-white">
                  Playtime Match
                </h3>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-400 mb-4 flex-1">
                671.2 hours is long, but matches your preference for longer
                games.
              </p>
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-yellow-50 dark:bg-yellow-500/10 border border-yellow-200 dark:border-yellow-500/20 text-yellow-600 dark:text-yellow-500 text-xs font-medium w-fit">
                <CheckCircle2 className="w-3.5 h-3.5" /> Good Match
              </div>
            </div>

            <div className="glass-card p-6 flex flex-col">
              <div className="flex items-center gap-2 mb-3">
                <Gamepad2 className="w-5 h-5 text-amber-500 dark:text-purple-400" />
                <h3 className="font-semibold text-slate-900 dark:text-white">
                  Genre Match
                </h3>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-400 mb-4 flex-1">
                Action is exactly your preferred genre.
              </p>
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/20 text-emerald-600 dark:text-emerald-400 text-xs font-medium w-fit">
                <CheckCircle2 className="w-3.5 h-3.5" /> Perfect Match
              </div>
            </div>
          </div>

          <div className="glass-card p-4 flex items-center justify-center gap-2 text-sm text-slate-600 dark:text-slate-300">
            <Star className="w-4 h-4 text-yellow-500 fill-yellow-500" />
            Overall, this game is an excellent match for your preferences!
          </div>
        </div>
      </div>
    </div>);

}
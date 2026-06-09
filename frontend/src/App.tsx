import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Stethoscope, Send, Trash2, User, Activity, Ruler, Hash, Moon, Sun } from 'lucide-react';
import './App.css';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

interface Profile {
  age: number;
  weight: number;
  height: number;
  gender: string;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [theme, setTheme] = useState<'light' | 'dark'>('dark');
  const [profile, setProfile] = useState<Profile>({
    age: 25,
    weight: 70,
    height: 175,
    gender: 'Male'
  });

  const chatEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;

    const userMsg: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: input,
          history: messages,
          profile: profile
        })
      });

      if (!response.ok) throw new Error('Failed to fetch');

      const data = await response.json();
      const aiMsg: Message = { role: 'assistant', content: data.output };
      setMessages(prev => [...prev, aiMsg]);
    } catch (error) {
      console.error(error);
      setMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, I encountered an error. Please check if the backend is running.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([]);
  };

  return (
    <div className="app-container">
      {/* Sidebar */}
      <aside className="sidebar">
        <h2>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Stethoscope /> Health AI
          </div>
          <button className="theme-toggle" onClick={toggleTheme}>
            {theme === 'light' ? <Moon size={20} /> : <Sun size={20} />}
          </button>
        </h2>
        <div className="profile-section">
          <h3>Patient Profile</h3>
          <div className="input-group">
            <label><Hash size={14} /> Age</label>
            <input 
              type="number" 
              value={profile.age} 
              onChange={e => setProfile({...profile, age: parseInt(e.target.value)})}
            />
          </div>
          <div className="input-group">
            <label><Activity size={14} /> Weight (kg)</label>
            <input 
              type="number" 
              value={profile.weight} 
              onChange={e => setProfile({...profile, weight: parseInt(e.target.value)})}
            />
          </div>
          <div className="input-group">
            <label><Ruler size={14} /> Height (cm)</label>
            <input 
              type="number" 
              value={profile.height} 
              onChange={e => setProfile({...profile, height: parseInt(e.target.value)})}
            />
          </div>
          <div className="input-group">
            <label><User size={14} /> Gender</label>
            <select 
              value={profile.gender} 
              onChange={e => setProfile({...profile, gender: e.target.value})}
            >
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>
          <button className="btn-outline" onClick={clearChat}>
            <Trash2 size={16} /> Clear Chat
          </button>
        </div>
        <p className="disclaimer">
          I am an AI, not a doctor. Please consult a healthcare professional for medical advice.
        </p>
      </aside>

      {/* Main Chat Area */}
      <main className="main-content">
        <div className="chat-container">
          {messages.length === 0 && (
            <div className="ai-message message">
              Hello! I am your AI Health Assistant. How can I help you today?
            </div>
          )}
          {messages.map((msg, i) => (
            <div key={i} className={`message ${msg.role === 'user' ? 'user-message' : 'ai-message'}`}>
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {msg.content}
              </ReactMarkdown>
            </div>
          ))}
          {isLoading && <div className="loading">Thinking...</div>}
          <div ref={chatEndRef} />
        </div>

        <div className="input-area">
          <input 
            type="text" 
            placeholder="Type your health query..." 
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyPress={e => e.key === 'Enter' && handleSend()}
          />
          <button className="btn-primary" onClick={handleSend} disabled={isLoading}>
            <Send size={18} />
          </button>
        </div>
      </main>
    </div>
  );
}

export default App;

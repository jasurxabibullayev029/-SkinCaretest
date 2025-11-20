# SkinCare AI - AI-Driven Skin Routine Assistant

A comprehensive skincare application that uses AI to help users determine their skin type, create personalized routines, track progress, and get expert advice.

## Features

### 🧴 Skin Type Quiz
- Interactive quiz to determine skin type (dry, oily, combination, sensitive, normal)
- 5-7 questions covering skin concerns, lifestyle, and preferences
- AI-powered analysis and personalized recommendations

### 🌞 AI Routine Generator
- Personalized daily/weekly skincare routines
- AI considers skin type, weather, stress levels, and diet
- Customizable routines with product recommendations

### 📊 Progress Tracker
- Photo upload and comparison (before/after)
- Skin metrics tracking (hydration, oiliness, redness, acne, wrinkles, pores)
- AI analysis of skin condition changes
- Visual progress charts

### 🤖 AI Chatbot (Skin Guru)
- Natural language conversations about skincare
- Personalized advice based on user profile
- 24/7 availability for skincare questions

### 📚 Knowledge Base
- Comprehensive articles on skincare topics
- Categorized content (skin types, ingredients, seasonal care)
- Search functionality and favorites
- User comments and community features

### 🎨 Modern UI/UX
- Responsive design for all devices
- Dark/light mode support
- Pastel color scheme (beige, white, soft pink, mint, blue)
- Smooth animations and transitions

## Tech Stack

### Backend
- **Python 4.2+** with Django
- **Django REST Framework** for API
- **PostgreSQL** database
- **OpenAI API** for AI features
- **Pillow** for image processing

### Frontend
- **React 18** with hooks
- **TailwindCSS** for styling
- **React Router** for navigation
- **Axios** for API calls
- **React Query** for state management
- **Chart.js** for progress visualization

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL (optional, SQLite for development)

### Backend Setup

1. **Clone and navigate to the project:**
```bash
git clone <repository-url>
cd skincare-ai
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Environment variables:**
```bash
cp .env.example .env
# Edit .env with your OpenAI API key and database settings
```

**Important: OpenAI API Setup**
1. Get an OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Edit the `.env` file and replace `your-openai-api-key-here` with your actual API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```
3. **Note:** If the OpenAI API key is not set, the chatbot will provide basic responses instead of AI-powered answers.

5. **Database setup:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Run the server:**
```bash
python manage.py runserver
```

### Frontend Setup

1. **Install dependencies:**
```bash
cd frontend
npm install
```

2. **Environment variables:**
```bash
# Create .env file in frontend directory
REACT_APP_API_URL=http://localhost:8000/api
```

3. **Start development server:**
```bash
npm start
```

## Usage

1. **Register/Login** to create your profile
2. **Take the Skin Quiz** to determine your skin type
3. **Generate personalized routines** using AI
4. **Track your progress** with photos and metrics
5. **Chat with Skin Guru** for expert advice
6. **Read articles** and learn about skincare

## API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/login/` - User login
- `GET /api/profile/` - Get user profile
- `PATCH /api/profile/` - Update user profile

### Quiz
- `GET /api/questions/` - Get quiz questions
- `POST /api/submit/` - Submit quiz answers
- `GET /api/results/` - Get quiz results

### Routines
- `GET /api/routines/` - Get user routines
- `POST /api/routines/` - Create routine
- `POST /api/generate-routine/` - Generate AI routine

### Tracker
- `GET /api/entries/` - Get progress entries
- `POST /api/entries/` - Create progress entry

### Articles
- `GET /api/articles/` - Get articles
- `GET /api/articles/{slug}/` - Get article detail
- `POST /api/articles/{id}/favorite/` - Toggle favorite

### Chatbot
- `POST /api/sessions/` - Create chat session
- `POST /api/chat/` - Send message

## Project Structure

```
skincare-ai/
├── accounts/          # User authentication
├── quiz/             # Skin type quiz
├── routines/         # Routine management
├── tracker/          # Progress tracking
├── articles/         # Knowledge base
├── chatbot/          # AI chatbot
├── frontend/         # React frontend
└── requirements.txt  # Python dependencies
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if necessary
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions:
- Email: support@skincare.ai
- Documentation: [Link to docs]

## Roadmap

- [ ] Mobile app development
- [ ] Advanced AI skin analysis
- [ ] Integration with skincare products API
- [ ] Community features
- [ ] Multi-language support

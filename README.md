# KDM Care Hospital - AI Multimodal Disease Prediction System

A comprehensive healthcare AI system that predicts 6 different diseases using machine learning models with a modern React frontend and FastAPI backend.

## 🏥 Features

- **6 Disease Prediction Models**:
  - Heart Disease (Tabular)
  - Diabetes (Tabular)
  - Brain Tumor Detection (Image - MobileNetV2)
  - Pneumonia Detection (Image - MobileNetV2)
  - Skin Cancer Detection (Image - MobileNetV2)
  - Eye Disease Detection (Image - MobileNetV2)

- **Patient Management System**
- **Reports Dashboard with PDF Export**
- **User Authentication**
- **Password Reset with Email Notifications**
- **Real-time AI Predictions**
- **Professional Medical Report Generation**

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PyTorch** - Deep learning framework
- **Scikit-learn & XGBoost** - ML models
- **MongoDB** - Database
- **Motor** - Async MongoDB driver
- **FastAPI-Mail** - Email service
- **ReportLab** - PDF generation

### Frontend
- **React** - UI framework
- **Vite** - Build tool
- **React Router** - Navigation
- **Tailwind CSS** - Styling
- **Material Symbols** - Icons

## 📋 Prerequisites

- Python 3.12+
- Node.js 18+
- MongoDB
- CUDA-capable GPU (optional, for training)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Milind1234-cpu/MULTIMODEL-DISEASE-PREDICTION.git
cd MULTIMODEL-DISEASE-PREDICTION
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env with your configuration:
# - MongoDB URI
# - Email credentials (for password reset)
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

### 4. Train ML Models (Optional)

```bash
cd backend

# Train tabular models (Heart Disease & Diabetes)
python ml/train_tabular.py

# Train image models (requires datasets)
python ml/train_image_models.py --disease brain-tumor
python ml/train_image_models.py --disease pneumonia
python ml/train_image_models.py --disease skin-cancer
python ml/train_image_models.py --disease eye-disease
```

**Note**: Pre-trained models are not included in the repository due to size. You need to train them or download datasets.

## 🎯 Running the Application

### Start Backend Server

```bash
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Start Frontend Server

```bash
cd frontend
npm run dev
```

### Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📧 Email Configuration

To enable password reset emails, configure SMTP settings in `backend/.env`:

```env
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_FROM=your-email@gmail.com
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
```

For Gmail, generate an App Password at: https://myaccount.google.com/apppasswords

## 📊 Dataset Information

### Tabular Datasets (Auto-downloaded)
- **Heart Disease**: UCI Heart Disease Cleveland
- **Diabetes**: Pima Indians Diabetes

### Image Datasets (Manual download required)
- **Brain Tumor**: Kaggle - Brain Tumor MRI Dataset
- **Pneumonia**: Kaggle - Chest X-Ray Images (Pneumonia)
- **Skin Cancer**: Kaggle - Skin Cancer MNIST: HAM10000
- **Eye Disease**: Kaggle - Ocular Disease Recognition

Place datasets in `backend/data/{disease}/train` and `backend/data/{disease}/val`

## 🏗️ Project Structure

```
.
├── backend/
│   ├── ml/                 # ML models and training scripts
│   ├── routers/            # API endpoints
│   ├── models/             # Trained model files
│   ├── data/               # Training datasets
│   ├── main.py             # FastAPI application
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── context/        # React context
│   ├── package.json        # Node dependencies
│   └── vite.config.js      # Vite configuration
└── README.md
```

## 🔒 Security Notes

- Never commit `.env` files with real credentials
- Use environment variables for sensitive data
- Model files are excluded from git (large files)
- Datasets are excluded from git (large files)

## 📝 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/forgot-password` - Request password reset
- `POST /api/auth/reset-password` - Reset password with token

### Patients
- `GET /api/patients` - Get all patients
- `POST /api/patients` - Create new patient

### Predictions
- `POST /api/predict/{disease_id}` - Make disease prediction

### Reports
- `GET /api/reports` - Get all reports
- `GET /api/reports/{report_id}/pdf` - Download PDF report

### Models
- `GET /api/models/status` - Check model status

## 🎨 Features Showcase

- ✅ Real-time AI predictions with confidence scores
- ✅ Professional PDF report generation
- ✅ Email notifications for password reset
- ✅ Responsive Material Design UI
- ✅ Patient management system
- ✅ Historical reports dashboard
- ✅ Image upload with drag-and-drop
- ✅ Form validation and error handling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Milind Lanje**
- GitHub: [@Milind1234-cpu](https://github.com/Milind1234-cpu)
- Email: blackgear2005@gmail.com

## 🙏 Acknowledgments

- UCI Machine Learning Repository for datasets
- Kaggle community for medical imaging datasets
- FastAPI and React communities

---

**Note**: This is an educational project. Always consult qualified medical professionals for actual medical diagnoses.

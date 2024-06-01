const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection
const uri = 'mongodb+srv://Bhargavi:BhbTwwe5UaJ2SbaP@atlascluster.0ix34gl.mongodb.net/MERNLoginGoogle?retryWrites=true&w=majority&appName=AtlasCluster'; // Your MongoDB URI from .env file
mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Email schema and model
const emailSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  subject: String,
  priority: String,
  status: String,
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const Email = mongoose.model('Email', emailSchema);

// Routes
// Fetch all emails
app.get('/emails', async (req, res) => {
  try {
    const emails = await Email.find();
    res.json(emails);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Fetch email by email address
app.get('/emails/:email', async (req, res) => {
  const { email } = req.params;
  try {
    const emailDetails = await Email.findOne({ email });
    if (!emailDetails) {
      return res.status(404).json({ message: 'Email not found' });
    }
    res.json(emailDetails);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port: ${port}`);
});

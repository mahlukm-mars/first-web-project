const express = require('express');
const path = require('path');
const app = express();

const PORT = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'public')));

// simple api to store "claimed issues" in memory (demo only)
app.use(express.json());
let claimed = [];

app.post('/api/claim', (req, res) => {
  const { name, issue } = req.body || {};
  if (!name || !issue) return res.status(400).json({ error: 'name and issue are required' });
  const entry = { id: Date.now(), name, issue, time: new Date().toISOString() };
  claimed.push(entry);
  res.json({ success: true, entry });
});

app.get('/api/claimed', (req, res) => {
  res.json({ claimed });
});

app.listen(PORT, () => {
  console.log(`Hacktober starter running at http://localhost:${PORT}`);
});

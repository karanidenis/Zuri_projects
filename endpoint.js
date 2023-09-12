module.exports = (req, res) => {
  const { query } = req;
  res.json({ query });
};

import React, { useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts';
import { BASE_URL } from './constant';

function MarketAnalysisDashboard() {
  const [productName, setProductName] = useState('');
  const [analysisResults, setAnalysisResults] = useState(null);

  const handleAnalysis = async () => {
    try {
      const response = await axios.post(`${BASE_URL}/analyze`, { product_name: productName });
      setAnalysisResults(response.data);
    } catch (error) {
      console.error('Analysis failed', error);
    }
  };

  // Transform data for chart
  const chartData = analysisResults?.sentiment_analysis?.map((item, index) => ({
    source: `Source ${index + 1}`,
    confidence: item.confidence * 100 // Convert to percentage
  })) || [];

  return (
    <div>
      <input
        value={productName}
        onChange={(e) => setProductName(e.target.value)}
        placeholder="Enter Product Name"
      />
      <button onClick={handleAnalysis}>Analyze</button>

      {analysisResults && (
        <div>
          <h2>Sentiment Analysis for {productName}</h2>
          <LineChart width={600} height={300} data={chartData}>
            <XAxis dataKey="source" />
            <YAxis />
            <Tooltip />
            <Line
              type="monotone"
              dataKey="confidence"
              stroke="#8884d8"
            />
          </LineChart>
        </div>
      )}
    </div>
  );
}

export default MarketAnalysisDashboard;
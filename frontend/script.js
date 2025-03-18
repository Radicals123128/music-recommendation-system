// API endpoint
const API_URL = 'http://127.0.0.1:5000';

// Function to get recommendations
async function getRecommendations() {
    const songInput = document.getElementById('songInput');
    const recommendationsList = document.getElementById('recommendations');
    const songName = songInput.value.trim();

    if (!songName) {
        showError('Please enter a song name!');
        return;
    }

    try {
        // Show loading state
        recommendationsList.innerHTML = '<li class="loading">Loading recommendations...</li>';

        const response = await fetch(`${API_URL}/recommend?song=${encodeURIComponent(songName)}`);
        const data = await response.json();

        // Clear previous results
        recommendationsList.innerHTML = '';

        if (data.recommendations === "Song not found") {
            showError('Song not found. Please try another one!');
            return;
        }

        // Display recommendations
        data.recommendations.forEach((song, index) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <div class="song-info">
                    <h3>${index + 1}. ${song.name}</h3>
                    <div class="song-details">
                        <p><strong>Singer:</strong> ${song.singer}</p>
                        <p><strong>Movie/Album:</strong> ${song.movie}</p>
                        <p><strong>Genre:</strong> ${song.genre}</p>
                        <p><strong>Rating:</strong> ${song.rating}</p>
                    </div>
                </div>
            `;
            recommendationsList.appendChild(li);
        });

    } catch (error) {
        console.error('Error fetching recommendations:', error);
        showError('Failed to fetch recommendations. Please try again later.');
    }
}

// Function to show error messages
function showError(message) {
    const recommendationsList = document.getElementById('recommendations');
    recommendationsList.innerHTML = `<li class="error">${message}</li>`;
}

// Add event listener for Enter key
document.getElementById('songInput').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        getRecommendations();
    }
}); 
response_form_mail = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Feedback Form</title>
            <style>
                body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            width: 300px;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
        }

        h3 {
            text-align: center;
        }

        form {
            margin-top: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
        }

        input[type="text"],
        input[type="email"] {
            width: calc(100% - 16px);
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .status input[type="radio"] {
            display: none;
        }

        .status label, .stars label {
            cursor: pointer;
            color: #555; /* Changed color to a darker shade */
            font-weight: bold; /* Added font weight */
        }

        .status label:hover,
        .status input[type="radio"]:checked ~ label,
        .stars label:hover,
        .stars input[type="radio"]:checked ~ label {
            color: orange;
        }

        .status.green label:hover,
        .status.green input[type="radio"]:checked ~ label,
        .stars.green label:hover,
        .stars.green input[type="radio"]:checked ~ label {
            color: green;
        }

        .status label::before {
            content: "\2605"; 
            margin-right: 5px;
        }

        .stars {
            display: flex;
            font-size: 24px;
            cursor: pointer;
        }

        .stars input {
            display: none;
        }

        .stars label {
            margin-right: 5px;
            color: #555;
            font-size: 28px; /* Increased font size for emojis */
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            float: right;
        }

        button:hover {
            background-color: #45a049;
        }
            </style>
        </head>
        <body>
            <div class="container">
            <div class="main">
                <h3>Give your feedback</h3>
                <form method="post" id="form">
                    <div class="form-outer">
                        <label>Problem Status:</label><br>
                        <div class="status">
                            <input type="radio" id="Solved" name="status"
                                value="solved"><label for="Solved">Problem
                                Solved &#128522;</label>
                            <input type="radio" id="NotSolved" name="status"
                                value="not_solved"><label
                                for="NotSolved">Problem Not solved
                                &#128533;</label><br>
                        </div>
                    </div>
                    <div class="form-outer">
                        <label>Rating for the Problem Solved:</label>
                        <div class="stars">
                            <input type="radio" id="star1" name="rating"
                                value="1"><label for="star1"
                                title="1 star">&#9733;</label>
                            <input type="radio" id="star2" name="rating"
                                value="2"><label for="star2"
                                title="2 stars">&#9733;</label>
                            <input type="radio" id="star3" name="rating"
                                value="3"><label for="star3"
                                title="3 stars">&#9733;</label>
                            <input type="radio" id="star4" name="rating"
                                value="4"><label for="star4"
                                title="4 stars">&#9733;</label>
                            <input type="radio" id="star5" name="rating"
                                value="5"><label for="star5"
                                title="5 stars">&#9733;</label>
                        </div>
                    </div>
                    <div class="form-outer">
                        <label>Problem Type:</label>
                        <input type="text" name="issue">
                    </div>
                    <div class="form-outer">
                        <label>Email:</label>
                        <input type="email" name="email">
                    </div>
                    <div>
                        <button type="submit">Submit</button>
                    </div>
                </form>
            </div>
        </div>
        <script>
        
        const statusSolved = document.getElementById('Solved');
        const statusNotSolved = document.getElementById('NotSolved');
    
        statusSolved.addEventListener('change', () => {
            if (statusSolved.checked) {
                statusSolved.nextElementSibling.style.color = 'orange';
                statusNotSolved.nextElementSibling.style.color = '#aaa';
            }
        });
    
        statusNotSolved.addEventListener('change', () => {
            if (statusNotSolved.checked) {
                statusNotSolved.nextElementSibling.style.color = 'orange';
                statusSolved.nextElementSibling.style.color = '#aaa';
            }
        });
    
        // Star rating radio button event listeners
        const stars = document.querySelectorAll('.stars input');
    
        stars.forEach(star => {
            star.addEventListener('change', () => {
                const selectedStar = parseInt(star.value);
    
                stars.forEach((s, index) => {
                    const label = s.nextElementSibling;
                    if (index < selectedStar) {
                        label.style.color = 'orange';
                    } else {
                        label.style.color = '#aaa';
                    }
                });
            });
        });
    
     
        const url = 'https://script.google.com/macros/s/AKfycbyuOeboD1uX0Jk9LBD5Pd3jddppuFDqLfU40z23jrmqfdXLF3B-jpo_fKQesX3tT_R-cQ/exec';
        const form = document.querySelector('#form');
    
        form.addEventListener('submit', (e) => {
            e.preventDefault(); 
    
            const formData = new FormData(form);
    
            fetch(url, {
                method: 'POST',
                body: formData
            })
            .then(response => response.text()) 
            .then(data => {
                console.log(data); 
                form.reset();
            })
            .catch(error => {
                console.error('Error:', error); 
            });
        });
    </script>
        </body>
        </html>
        """
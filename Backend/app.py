from flask import Flask, jsonify, send_file, make_response
import os

app = Flask(__name__)

@app.route('/api/endpoint', methods=['GET'])
def get_image():
    # Define the path to the image file on your PC using forward slashes
    #image_url = 'https://www.corinthiantravel.co.uk/blog/wp-content/uploads/2016/07/Everything-you-need-to-know-when-visiting-the-Pyramids-in-Cairo-Egypt.jpg'  # Update the filename as needed

    image_path = 'OneDrive\\Pictures\\Saved Pictures\\pyramid_image.jpeg'

    

    # Check if the request was successful (status code 200)
    if os.path.exists(image_path):
        # Return the image as a file attachment
        with open(image_path, 'rb') as image_file:
            # Read the image data
            image_data = image_file.read()
        
        # Create a Flask response with the image data and appropriate content type
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpeg'  # Adjust the content type as needed (e.g., image/png for PNG images)

        return response
        #return send_file(image_path, as_attachment=True)
    else:
        return jsonify({"error": "Image not found"}, 404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
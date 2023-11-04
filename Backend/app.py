{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9a51de7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [04/Nov/2023 20:15:22] \"GET /api/endpoint HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, jsonify, send_file, make_response\n",
    "import os\n",
    "import requests\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/api/endpoint', methods=['GET'])\n",
    "def get_image():\n",
    "    # Define the path to the image file on your PC using forward slashes\n",
    "    #image_url = 'https://www.corinthiantravel.co.uk/blog/wp-content/uploads/2016/07/Everything-you-need-to-know-when-visiting-the-Pyramids-in-Cairo-Egypt.jpg'  # Update the filename as needed\n",
    "\n",
    "    image_path = 'OneDrive\\\\Pictures\\\\Saved Pictures\\\\pyramid_image.jpeg'\n",
    "\n",
    "    \n",
    "\n",
    "    # Check if the request was successful (status code 200)\n",
    "    if os.path.exists(image_path):\n",
    "        # Return the image as a file attachment\n",
    "        with open(image_path, 'rb') as image_file:\n",
    "            # Read the image data\n",
    "            image_data = image_file.read()\n",
    "        \n",
    "        # Create a Flask response with the image data and appropriate content type\n",
    "        response = make_response(image_data)\n",
    "        response.headers['Content-Type'] = 'image/jpeg'  # Adjust the content type as needed (e.g., image/png for PNG images)\n",
    "\n",
    "        return response\n",
    "        #return send_file(image_path, as_attachment=True)\n",
    "    else:\n",
    "        return jsonify({\"error\": \"Image not found\"}, response)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8f098de",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b9482c6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

def checkLeftRight(image, results, draw=False, display=False):
    '''

    This function finds the horizontal position (left, center, right) of the person in an image.

    Args:

        image:   The input image with a prominent person whose the horizontal position needs to be found.

        results: The output of the pose landmarks detection on the input image.

        draw:    A boolean value that is if set to true the function writes the horizontal position on the output image.

        display: A boolean value that is if set to true the function displays the resultant image and returns nothing.

    Returns:

        output_image:         The same input image but with the horizontal position written, if it was specified.

        horizontal_position:  The horizontal position (left, center, right) of the person in the input image.

    '''

    # Declare a variable to store the horizontal position (left, center, right) of the person.

    horizontal_position = None

    # Get the height and width of the image.

    height, width, _ = image.shape

    # Create a copy of the input image to write the horizontal position on.

    output_image = image.copy()

    # Retreive the x-coordinate of the left shoulder landmark.

    left_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width)

    # Retreive the x-corrdinate of the right shoulder landmark.

    right_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * width)

    # Check if the person is at left that is when both shoulder landmarks x-corrdinates

    # are less than or equal to the x-corrdinate of the center of the image.

    if (right_x <= width // 2 and left_x <= width // 2):

        # Set the person's position to left.

        horizontal_position = 'Left'



    # Check if the person is at right that is when both shoulder landmarks x-corrdinates

    # are greater than or equal to the x-corrdinate of the center of the image.

    elif (right_x >= width // 2 and left_x >= width // 2):

        # Set the person's position to right.

        horizontal_position = 'Right'



    # Check if the person is at center that is when right shoulder landmark x-corrdinate is greater than or equal to

    # and left shoulder landmark x-corrdinate is less than or equal to the x-corrdinate of the center of the image.

    elif (right_x >= width // 2 and left_x <= width // 2):

        # Set the person's position to center.

        horizontal_position = 'Center'

    # Check if the person's horizontal position and a line at the center of the image is specified to be drawn.

    if draw:
        # Write the horizontal position of the person on the image.

        cv2.putText(output_image, horizontal_position, (5, height - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

        # Draw a line at the center of the image.

        cv2.line(output_image, (width // 2, 0), (width // 2, height), (255, 255, 255), 2)

    # Check if the output image is specified to be displayed.

    if display:

        # Display the output image.

        plt.figure(figsize=[10, 10])

        plt.imshow(output_image[:, :, ::-1]);
        plt.title("Output Image");
        plt.axis('off');



    # Otherwise

    else:

        # Return the output image and the person's horizontal position.

        return output_image, horizontal_position
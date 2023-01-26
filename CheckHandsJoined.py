def checkHandsJoined(image, results, draw=False, display=False):
    '''

    This function checks whether the hands of the person are joined or not in an image.

    Args:

        image:   The input image with a prominent person whose hands status (joined or not) needs to be classified.

        results: The output of the pose landmarks detection on the input image.

        draw:    A boolean value that is if set to true the function writes the hands status & distance on the output image.

        display: A boolean value that is if set to true the function displays the resultant image and returns nothing.

    Returns:

        output_image: The same input image but with the classified hands status written, if it was specified.

        hand_status:  The classified status of the hands whether they are joined or not.

    '''

    # Get the height and width of the input image.

    height, width, _ = image.shape

    # Create a copy of the input image to write the hands status label on.

    output_image = image.copy()

    # Get the left wrist landmark x and y coordinates.

    left_wrist_landmark = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * width,

                           results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height)

    # Get the right wrist landmark x and y coordinates.

    right_wrist_landmark = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width,

                            results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height)

    # Calculate the euclidean distance between the left and right wrist.

    euclidean_distance = int(hypot(left_wrist_landmark[0] - right_wrist_landmark[0],

                                   left_wrist_landmark[1] - right_wrist_landmark[1]))

    # Compare the distance between the wrists with a appropriate threshold to check if both hands are joined.

    if euclidean_distance < 130:

        # Set the hands status to joined.

        hand_status = 'Hands Joined'

        # Set the color value to green.

        color = (0, 255, 0)



    # Otherwise.

    else:

        # Set the hands status to not joined.

        hand_status = 'Hands Not Joined'

        # Set the color value to red.

        color = (0, 0, 255)

    # Check if the Hands Joined status and hands distance are specified to be written on the output image.

    if draw:
        # Write the classified hands status on the image.

        cv2.putText(output_image, hand_status, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 3)

        # Write the the distance between the wrists on the image.

        cv2.putText(output_image, f'Distance: {euclidean_distance}', (10, 70),

                    cv2.FONT_HERSHEY_PLAIN, 2, color, 3)

    # Check if the output image is specified to be displayed.

    if display:

        # Display the output image.

        plt.figure(figsize=[10, 10])

        plt.imshow(output_image[:, :, ::-1]);
        plt.title("Output Image");
        plt.axis('off');



    # Otherwise

    else:

        # Return the output image and the classified hands status indicating whether the hands are joined or not.

        return output_image, hand_status
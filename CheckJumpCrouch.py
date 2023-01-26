def checkJumpCrouch(image, results, MID_Y=250, draw=False, display=False):
    '''

    This function checks the posture (Jumping, Crouching or Standing) of the person in an image.

    Args:

        image:   The input image with a prominent person whose the posture needs to be checked.

        results: The output of the pose landmarks detection on the input image.

        MID_Y:   The intial center y-coordinate of both shoulders landmarks of the person recorded during starting

                 the game. This will give the idea of the person's height when he is standing straight.

        draw:    A boolean value that is if set to true the function writes the posture on the output image.

        display: A boolean value that is if set to true the function displays the resultant image and returns nothing.

    Returns:

        output_image: The input image with the person's posture written, if it was specified.

        posture:      The posture (Jumping, Crouching or Standing) of the person in an image.

    '''

    # Get the height and width of the image.

    height, width, _ = image.shape

    # Create a copy of the input image to write the posture label on.

    output_image = image.copy()

    # Retreive the y-coordinate of the left shoulder landmark.

    left_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height)

    # Retreive the y-coordinate of the right shoulder landmark.

    right_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * height)

    # Calculate the y-coordinate of the mid-point of both shoulders.

    actual_mid_y = abs(right_y + left_y) // 2

    # Calculate the upper and lower bounds of the threshold.

    lower_bound = MID_Y - 15

    upper_bound = MID_Y + 100

    # Check if the person has jumped that is when the y-coordinate of the mid-point

    # of both shoulders is less than the lower bound.

    if (actual_mid_y < lower_bound):

        # Set the posture to jumping.

        posture = 'Jumping'



    # Check if the person has crouched that is when the y-coordinate of the mid-point

    # of both shoulders is greater than the upper bound.

    elif (actual_mid_y > upper_bound):

        # Set the posture to crouching.

        posture = 'Crouching'



    # Otherwise the person is standing and the y-coordinate of the mid-point

    # of both shoulders is between the upper and lower bounds.

    else:

        # Set the posture to Standing straight.

        posture = 'Standing'

    # Check if the posture and a horizontal line at the threshold is specified to be drawn.

    if draw:
        # Write the posture of the person on the image.

        cv2.putText(output_image, posture, (5, height - 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

        # Draw a line at the intial center y-coordinate of the person (threshold).

        cv2.line(output_image, (0, MID_Y), (width, MID_Y), (255, 255, 255), 2)

    # Check if the output image is specified to be displayed.

    if display:

        # Display the output image.

        plt.figure(figsize=[10, 10])

        plt.imshow(output_image[:, :, ::-1]);
        plt.title("Output Image");
        plt.axis('off');



    # Otherwise

    else:

        # Return the output image and posture indicating whether the person is standing straight or has jumped, or crouched.

        return output_image, posture
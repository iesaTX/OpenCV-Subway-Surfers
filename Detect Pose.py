def detectPose(image, pose, draw=False, display=False):
    '''

    This function performs the pose detection on the most prominent person in an image.

    Args:

        image:   The input image with a prominent person whose pose landmarks needs to be detected.

        pose:    The pose function required to perform the pose detection.

        draw:    A boolean value that is if set to true the function draw pose landmarks on the output image.

        display: A boolean value that is if set to true the function displays the original input image, and the

                 resultant image and returns nothing.

    Returns:

        output_image: The input image with the detected pose landmarks drawn if it was specified.

        results:      The output of the pose landmarks detection on the input image.

    '''

    # Create a copy of the input image.

    output_image = image.copy()

    # Convert the image from BGR into RGB format.

    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform the Pose Detection.

    results = pose.process(imageRGB)

    # Check if any landmarks are detected and are specified to be drawn.

    if results.pose_landmarks and draw:
        # Draw Pose Landmarks on the output image.

        mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,

                                  connections=mp_pose.POSE_CONNECTIONS,

                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255),

                                                                               thickness=3, circle_radius=3),

                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49, 125, 237),

                                                                                 thickness=2, circle_radius=2))

    # Check if the original input image and the resultant image are specified to be displayed.

    if display:

        # Display the original input image and the resultant image.

        plt.figure(figsize=[22, 22])

        plt.subplot(121);
        plt.imshow(image[:, :, ::-1]);
        plt.title("Original Image");
        plt.axis('off');

        plt.subplot(122);
        plt.imshow(output_image[:, :, ::-1]);
        plt.title("Output Image");
        plt.axis('off');



    # Otherwise

    else:

        # Return the output image and the results of pose landmarks detection.

        return output_image, results
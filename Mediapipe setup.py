# Initialize mediapipe pose class.

mp_pose = mp.solutions.pose



# Setup the Pose function for images.

pose_image = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)



# Setup the Pose function for videos.

pose_video = mp_pose.Pose(static_image_mode=False, model_complexity=1, min_detection_confidence=0.7,

                         min_tracking_confidence=0.7)



# Initialize mediapipe drawing class.

mp_drawing = mp.solutions.drawing_utils
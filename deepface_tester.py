from deepface import DeepFace
face_analysis = DeepFace.analyze(img_path = "tester.jpeg")
print(face_analysis["emotion"])
print(face_analysis["dominant_emotion"])

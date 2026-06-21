📸 AWS Image Recognition Pipeline
🏗️ Architecture
<img width="1536" height="1024" alt="ChatGPT Image Jun 21, 2026, 12_39_27 PM" src="https://github.com/user-attachments/assets/6c04447e-06cd-48bb-a540-44fff7578957" />


📌 Project Description

A fully serverless image recognition pipeline built using AWS services. When an image is uploaded to Amazon S3, it automatically triggers a Lambda function that calls Amazon Rekognition to detect objects, labels, and scenes. The results are stored in Amazon DynamoDB for future analysis and reporting.

⚙️ AWS Services Used
Amazon S3 – Stores uploaded images
AWS Lambda – Processes image events
Amazon Rekognition – Detects objects & labels
Amazon DynamoDB – Stores analysis results
Amazon CloudWatch – Logs execution flow
🔄 Project Workflow
Upload image to S3 bucket
S3 triggers Lambda function
Lambda sends image to Rekognition
Rekognition returns detected labels & confidence scores
Lambda stores results in DynamoDB
📸 Step-by-Step Screenshots (With Description)
1️⃣ Step 1: Upload Image to S3 Bucket

📌 Description: User uploads an image into the S3 bucket, which acts as the starting point of the pipeline.
<img width="1908" height="785" alt="Screenshot 2026-06-21 124408" src="https://github.com/user-attachments/assets/14d8d9da-5935-4428-b651-90b453b76f61" />


2️⃣ Step 2: S3 Event Trigger

📌 Description: S3 bucket automatically triggers the Lambda function when a new image is uploaded.
<img width="1918" height="761" alt="Screenshot 2026-06-21 124503" src="https://github.com/user-attachments/assets/b42f0e76-d711-4920-a6ce-8d966b3e21c5" />


3️⃣ Step 3: Lambda Function Execution

📌 Description: AWS Lambda processes the event and sends the image to Rekognition for analysis.
<img width="1886" height="788" alt="Screenshot 2026-06-21 124619" src="https://github.com/user-attachments/assets/3a7cafc2-28bd-49ce-b30d-224b1520340d" />


4️⃣ Step 4: Amazon Rekognition Analysis

📌 Description: Rekognition detects objects, scenes, and labels from the image with confidence scores.
<img width="1918" height="788" alt="Screenshot 2026-06-21 125022" src="https://github.com/user-attachments/assets/18940d0e-5b1b-44f0-8726-080b191c825a" />



5️⃣ Step 5: Store Results in DynamoDB

📌 Description: Lambda stores the extracted labels and metadata into DynamoDB for future queries.
<img width="1881" height="768" alt="Screenshot 2026-06-21 124742" src="https://github.com/user-attachments/assets/c6b09181-311d-41f5-b06c-d884b7966147" />


6️⃣ Step 6: CloudWatch Logs Verification

📌 Description: CloudWatch logs confirm successful execution of the entire pipeline.
<img width="1897" height="772" alt="Screenshot 2026-06-21 123748" src="https://github.com/user-attachments/assets/aef9a3a1-841f-430f-a188-776b5878d6bd" />


🚀 Final Output
Fully automated serverless image recognition system
Real-time object detection using AWS AI services
Scalable storage using DynamoDB
Event-driven architecture using S3 + Lambda

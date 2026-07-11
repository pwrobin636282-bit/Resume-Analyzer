import os
import pdfplumber
import pandas as pd

# Find files automatically even if the extensions are weird
all_files = os.listdir('.')
skills_file = next((f for f in all_files if 'skill' in f.lower() and f.endswith('.csv')), None)
jobs_file = next((f for f in all_files if 'job' in f.lower() and f.endswith('.csv')), None)

if not skills_file or not jobs_file:
    raise FileNotFoundError(f"Could not find your CSV files. Current files in folder: {all_files}")

# Load the automatically discovered files
skill_df = pd.read_csv(skills_file)
skill_list = skill_df['Skills'].tolist()



job_df = pd.read_csv(jobs_file)

def analyze_resume(resume_path):
    
        results=[]
        resume_text = ""

        with pdfplumber.open(resume_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    resume_text += text

        detected_skill = []
        for skill in skill_list:
            if skill.lower() in resume_text.lower():
                detected_skill.append(skill)
        recommendation=[]
        for index, row in job_df.iterrows():
            missing_skills = []
            matched_skills = []
            
            role_job = row['job role']
            role_skill = row['skills']
            
            role_skills = str(role_skill).split(',')
            match_count = 0
            for j in role_skills:
                j = j.strip()
                if j in detected_skill:
                    match_count += 1
                    matched_skills.append(j)
                else:
                    missing_skills.append(j)

            total_skills = len(role_skills)

            percentage = (match_count / total_skills) * 100

            recommendation.append(
                (
                role_job,
                match_count,
                percentage,
                missing_skills,
                matched_skills
                )
            )

        recommendation.sort(
            key=lambda x: x[2],
            reverse=True
        )

        
        for rank, (job, score, percentage, missing, matched) in enumerate(recommendation[:5], start=1):
            print(f"Rank {rank}")

            print("Job Role :", job)

            print("Match Count :", score)

            print("Match Percentage :", round(percentage,2),"%")

            print("Matched Skills :", matched)

            print("Missing Skills :", missing)

            print()
            results.append([
                os.path.basename(resume_path),
                rank,
                job,
                score,
                round(percentage,2),
                ", ".join(matched),
                ", ".join(missing)
            ])
            
    

        result_df = pd.DataFrame(
            results,
            columns=[
            "Resume",
            "Rank",
            "Recommended Job",
            "Match Count",
            "Match Percentage",
            "Matched Skills",
            "Missing Skills"
        ])

        result_df.to_csv(
            "recommendations.csv",
            index=False
        )

        print("Recommendations saved successfully!")
        return result_df
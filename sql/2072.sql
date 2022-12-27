SELECT student_id,score,'ny' uni FROM NewYork WHERE score >= 90
UNION
SELECT student_id,score,'ca' uni FROM California WHERE score >= 90;
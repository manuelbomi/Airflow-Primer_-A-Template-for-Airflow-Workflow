# Airflow-Primer: A Template for Speedy Prototyping Airflow Workflow


#### In this discourse, we present infographs that highlights how Airflow can be easily and speedliy installed on a Windows based computer. We also show how users can start working with Airflow by creating a file with Airflow DAGs that could be used to read some data from some API, store the data in a file, and read the data from that file. 

#### Install Airflow Astro CLI  on WIndows OS (using Powershell) by typing <ins>winget install -e --id Astronomer.Astro</ins>
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/37a0897d-8d1f-4085-b2b4-a81d658a0520" />

---

#### Install on windows using Powershell as an Admin
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/766ed043-11a1-4d02-a60f-484909511bc1" />

---

#### Verify installation via cmd by typing astro version. Then, create a new folder and type astro dev init to start up Airflow

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/99128c64-34c3-4113-91f2-eee2da62ee35" />

---

#### Type <ins>dir</ins> to see that all Airflow reqired folders av been generated

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/b7326170-b6ef-4ba4-ac9d-02e639351fcc" />

---

####   Type <ins>code .</ins> to open the Airflow folder on VSCode

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/13300702-bf5f-4ced-b4ad-0e85e6a6a5eb" />
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/61e1a6c2-07a2-4f87-9f18-59795b66621b" />

---

#### On the terminal of your project type <ins>astro dev</ins> start to start the project
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/1b074375-23e5-44f4-bc7a-a9aab7339c2b" />

---

#### Your astro project can now be accesses via localhost 8080
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/3f6ea135-46be-45b8-90c7-5bfff6f144e6" />
<img width="1347" height="507" alt="Image" src="https://github.com/user-attachments/assets/04e4c4b4-d301-4689-abda-d9cdab771767" />

---


#### Create a workflow to get some data from an API, write it to a file and read it from the file
On the repository, the workflow is available here: https://github.com/manuelbomi/An-Airflow-Primer-for-Airflow-Pipelines/blob/main/dags/some_activity.py

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/19467e11-d623-4373-8991-b45c943e9116" />

---

#### Create variable from user interface. Go to Admin, Variables
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/135586b3-7c57-45e9-9a2a-3d1f7eabe568" />

---

#### Click "Add Variables"
<img width="1297" height="503" alt="Image" src="https://github.com/user-attachments/assets/aa5f8491-8a00-4dce-91c7-c2da4e0447fe" />

---

####  Input key and val and click save

<img width="1313" height="494" alt="Image" src="https://github.com/user-attachments/assets/9bb67090-a4f0-48d4-bc43-182c8701ee3a" />
<img width="1315" height="493" alt="Image" src="https://github.com/user-attachments/assets/ab0a7525-2869-4894-826f-4a384c341fb5" />

---

#### Here is the designed workflow
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/3d2aff65-a9e0-433b-9e54-570a3fb934b7" />
<img width="1346" height="507" alt="Image" src="https://github.com/user-attachments/assets/e0eefe4a-1b1a-44c4-b564-1b78e0e7580b" />
<img width="1359" height="508" alt="Image" src="https://github.com/user-attachments/assets/3fa054e6-10d7-402b-b253-8c7587a64ada" />

---

#### Click to trigger the DAG

<img width="1282" height="497" alt="Image" src="https://github.com/user-attachments/assets/5d61a03f-fa4b-4790-a149-a7aeefc8c684" />

---

#### Successful DAG run
<img width="1333" height="695" alt="Image" src="https://github.com/user-attachments/assets/a2db8bac-a157-4358-b834-14b857d8ccbe" />
<img width="1338" height="694" alt="Image" src="https://github.com/user-attachments/assets/e336e543-edb4-4cb3-a795-5fe932d328e7" />











 

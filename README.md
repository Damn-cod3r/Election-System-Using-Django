# Election System App

## Overview
The **Election System App** is a simple and efficient voting platform designed to allow users to cast votes and view results in real-time. The app provides a straightforward interface where users can select a candidate and submit their vote. It also displays the total number of votes for each candidate.

## Features
- **Voting Interface**: Users can cast their vote for one of the available candidates.
- **Real-time Results**: After voting, users can view the total number of votes each candidate has received.
- **No Login Required**: The app currently does not require users to log in to cast a vote or view results, making the process quick and accessible.

## Screenshots
![image](https://github.com/user-attachments/assets/2466b7b6-df62-441f-ac22-604fa7173635)
![image](https://github.com/user-attachments/assets/39cbc35f-75df-49d1-9502-dd8122586db6)
![image](https://github.com/user-attachments/assets/7ec0b7fe-ea57-4b87-855f-a965ec0bd425)
![image](https://github.com/user-attachments/assets/47a926f6-986f-4f8e-9918-5bd939facd61)
![image](https://github.com/user-attachments/assets/07e5a3a2-4673-4748-8596-5f0f9177beba)
![image](https://github.com/user-attachments/assets/beee87f8-235e-431e-b5e3-b5edf130de2e)
![image](https://github.com/user-attachments/assets/803d1455-3589-41f0-b792-78ec93f4911a)

### Voting Screen
![image](https://github.com/user-attachments/assets/d1d5f2f6-da59-476e-8813-cc4e85847f73)

The voting screen displays a list of candidates (Person 1, Person 2, Person 3, Person 4). Users can select one candidate and submit their vote via the `Submit` button.  
URL: `http://127.0.0.1:8000/election/vote/`

### Results Screen
![image](https://github.com/user-attachments/assets/8ab35875-741c-4f63-9bbd-aac524dbce29)

After voting, users are directed to the results screen, which shows the total votes for each candidate.  
URL: `http://127.0.0.1:8000/election/results/`

## Example Results:
- Person 1: 20 votes
- Person 2: 30 votes
- Person 3: 5 votes
- Person 4: 7 votes

## Installation & Setup
1. Clone the repository or download the project files.
2. Ensure Python and Django are installed in your environment.
3. Run the following command to start the Django server:
    ```bash
    python manage.py runserver
    ```
4. Access the app by navigating to `http://127.0.0.1:8000/election/vote/` for voting and `http://127.0.0.1:8000/election/results/` for results.

## Future Enhancements
- **User Authentication**: Implement a login system to ensure that each user can vote only once.
- **Improved User Interface**: Enhance the visual design of the app for a more user-friendly experience.
- **Multiple Elections Support**: Add functionality to handle multiple elections and different voting types.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any issues or contributions, please contact chidambaram sekar at chidambaram097@gmail.com.

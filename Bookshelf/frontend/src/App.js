import { useEffect, useState } from 'react';
import axios from 'axios';
import { format } from 'date-fns';

import './App.css';

const baseUrl = 'http://localhost:5000';

function App() {
	const [ title, setTitle ] = useState('');
	const [ editTitle, seteditTitle ] = useState('');
	const [ author, setAuthor ] = useState('');
	const [ editAuthor, seteditAuthor ] = useState('');
	const [ genre, setGenre ] = useState('');
	const [ editGenre, seteditGenre ] = useState('');
	const [ eventsList, setEventsList ] = useState([]);
	const [ eventId, setEventId ] = useState(null);

	const fetchEvents = async () => {
		const data = await axios.get(`${baseUrl}/events`);
		const { events } = data.data;
		setEventsList(events);
	};

	const handlechangetitle = (e, field) => {
		if (field == 'edit') {
			seteditTitle(e.target.value);
		} else {
			setTitle(e.target.value);
		}
	};

	const handlechangeauthor = (e, field) => {
		if (field == 'edit') {
			seteditAuthor(e.target.value);
		} else {
			setAuthor(e.target.value);
		}
	};

	const handlechangegenre = (e, field) => {
		if (field == 'edit') {
			seteditGenre(e.target.value);
		} else {
			setGenre(e.target.value);
		}
	};

	const handleDelete = async (id) => {
		try {
			await axios.delete(`${baseUrl}/events/${id}`);
			const updatedList = eventsList.filter((event) => event.id !== id);
			setEventsList(updatedList);
		} catch (err) {
			console.error(err.message);
		}
	};

	const toggleEdit = (event) => {
		setEventId(event.id);
		seteditTitle(event.title);
		seteditAuthor(event.author);
		seteditGenre(event.genre);
	};

	const handleSubmit = async (e) => {
		e.preventDefault();
		try {
			if (editTitle) {
				const data = await axios.put(`${baseUrl}/events/${eventId}`, { title: editTitle });
				const updatedEvent = data.data.event;
				const updatedList = eventsList.map((event) => {
					if (event.id == eventId) {
						return (event = updatedEvent);
					}
					return event;
				});
				setEventsList(updatedList);
			} else if (editAuthor) {
				const data = await axios.put(`${baseUrl}/events/${eventId}`, { author: editAuthor });
				const updatedEvent = data.data.event;
				const updatedList = eventsList.map((event) => {
					if (event.id == eventId) {
						return (event = updatedEvent);
					}
					return event;
				});
				setEventsList(updatedList);
			} else if (editGenre) {
				const data = await axios.put(`${baseUrl}/events/${eventId}`, { genre: editGenre });
				const updatedEvent = data.data.event;
				const updatedList = eventsList.map((event) => {
					if (event.id == eventId) {
						return (event = updatedEvent);
					}
					return event;
				});
				setEventsList(updatedList);
			} else {
				const data = await axios.post(`${baseUrl}/events`, [ { title }, { author }, { genre } ]);
				setEventsList([ ...eventsList, data.data ]);
			}
			setTitle('');
			seteditTitle('');
			setAuthor('');
			seteditAuthor('');
			setGenre('');
			seteditGenre('');
			setEventId(null);
		} catch (err) {
			console.log(err.message);
		}
	};

	useEffect(() => {
		fetchEvents();
	}, []);

	return (
		<div className="App">
			<section>
				<form onSubmit={handleSubmit}>
					<label htmlFor="title">Title</label>
					<input
						onChange={(e) => handlechangetitle(e, 'title')}
						type="text"
						name="title"
						id="title"
						placeholder="Give the Book a Ttile"
						value={title}
					/>
					<br />
					<label htmlFor="author">Author</label>
					<input
						onChange={(e) => handlechangeauthor(e, 'author')}
						type="text"
						name="author"
						id="author"
						placeholder="Who wrote this book?"
						value={author}
					/>
					<br />
					<label htmlFor="genre">Genre</label>
					<input
						onChange={(e) => handlechangegenre(e, 'genre')}
						type="text"
						name="genre"
						id="genre"
						placeholder="What type of genre is this book from?"
						value={genre}
					/>
					<button type="submit">Submit</button>
				</form>
			</section>
			<section>
				<ul>
					{eventsList.map((event) => {
						if (eventId == event.id) {
							return (
								<li>
									<form onSubmit={handleSubmit} key={event.id}>
										<input
											onChange={(e) => handlechangetitle(e, 'edit')}
											type="text"
											name="editTitle"
											id="editTitle"
											value={editTitle}
										/>
										<input
											onChange={(e) => handlechangeauthor(e, 'edit')}
											type="text"
											name="editAuthor"
											id="editAuthor"
											value={editAuthor}
										/>
										<input
											onChange={(e) => handlechangegenre(e, 'edit')}
											type="text"
											name="editGenre"
											id="editGenre"
											value={editGenre}
										/>
										<button type="submit">Submit</button>
									</form>
								</li>
							);
						} else {
							return (
								<li style={{ display: 'flex' }} key={event.id}>
									{[ event.title, ', ', event.author, ', ', event.genre ]}
									<button onClick={() => toggleEdit(event)}>Edit</button>
									<button onClick={() => handleDelete(event.id)}>X</button>
								</li>
							);
						}
					})}
				</ul>
			</section>
		</div>
	);
}

export default App;

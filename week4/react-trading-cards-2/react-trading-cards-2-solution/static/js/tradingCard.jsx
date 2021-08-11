function TradingCard(props) {
  return (
    <div className="card">
      <p> Name: {props.name} </p>
      <img src={props.imgUrl} />
      <p> Skill: {props.skill} </p>
    </div>
  );
}

function AddTradingCard(props) {
  const [name, setName] = React.useState("");
  const [skill, setSkill] = React.useState("");
  function addNewCard() {
    fetch("/add-card", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, skill }),
    }).then((response) => {
      response.json().then((jsonResponse) => {
        const {
          cardAdded: { cardId, name, skill },
        } = jsonResponse; // same as cardId = jsonResponse.cardAdded.cardId and so on
        props.addCard(cardId, name, skill);
      });
    });
  }
  return (
    <React.Fragment>
      <h2>Add New Trading Card</h2>
      <label htmlFor="nameInput">Name</label>
      <input
        value={name}
        onChange={(event) => setName(event.target.value)}
        id="nameInput"
        style={{ marginLeft: "5px" }}
      ></input>
      <label
        htmlFor="skillInput"
        style={{ marginLeft: "10px", marginRight: "5px" }}
      >
        Skill
      </label>
      <input
        value={skill}
        onChange={(event) => setSkill(event.target.value)}
        id="skillInput"
      ></input>
      <button style={{ marginLeft: "10px" }} onClick={addNewCard}>
        Add
      </button>
    </React.Fragment>
  );
}

function TradingCardContainer() {
  const [cards, setCards] = React.useState([]);

  function addCardFunction(cardId, name, skill) {
    const imgUrl = 'static/img/placeholder.png'
    const newCard = { cardId, skill, name, imgUrl }; // equivalent to { cardId: cardId, skill: skill, name: name, imgUrl: imgUrl }
    const currentCards = [...cards, newCard]; // makes a copy of cards. similar to doing currentCards = cards[:] in Python
    // [...currentCards, newCard] is an array containing all elements in currentCards followed by newCard
    setCards(currentCards);
  }

  React.useEffect(() => {
    fetch("/cards.json")
      .then((response) => response.json())
      .then((data) => setCards(data.cards));
  }, []);

  const tradingCards = [];

  // you can uncomment this console.log (line 27) to see the
  // value of the cards object what is it initially?
  // what about after the component re-renders?
  // if you remove the empty array on line 18 (so
  // there is no dependency list, what happens?)
  // console.log({ cards });

  for (const currentCard of cards) {
    tradingCards.push(
      <TradingCard
        key={currentCard.cardId}
        name={currentCard.name}
        skill={currentCard.skill}
        imgUrl={currentCard.imgUrl}
      />
    );
  }

  return (
    <React.Fragment>
      <AddTradingCard addCard={addCardFunction} />
      <h2>Trading Cards</h2>
      <div className="grid">{tradingCards}</div>
    </React.Fragment>
  );
}

ReactDOM.render(<TradingCardContainer />, document.getElementById("container"));

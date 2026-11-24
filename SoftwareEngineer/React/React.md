# React \- The complete guide

Note from [React \- The Complete Guide (Includes Hooks, React Router, and Redux) \- Second Edition](https://learning.oreilly.com/course/react-the/9781801812603/)

## Getting Started

React is a JS **library**. Using JS typically is not a great option because:

- writing complex JS code quickly becomes cumbersome  
- complex JS is error-prone  
- complex JS is difficult to maintain and edit  
- React offers a simpler mental model

React is a **declarative** UI programming language, so you do not explain the step to update and create the UI like in vanilla JS. Vanilla JS is an imperative UI programming language.

JSX means html in JS. JSX cannot be read by the browser.

The code we write in React is not the code that is executed. The React code is transformed before it is read by the browser with the Build Process. This Build Process is done by a server. This Build Process optimizes the code. For instance it performs minimisation which shortens the name of the variables. That’s why [Node.Js](http://Node.Js) is needed to execute this Build Process.

## React Essentials \- Components, JSX, Props, State & More

### Components

Components are combinable UI components for a UI. They wrap js, html and css code. The advantage is that related codes (html, css and js) are combined together.  
![][image1]![][image2]  
![][image3]

### declaration

An example of a component code. React components are js functions which must start with upper case and return a renderable value. They must start with upper case to not clash with standard DOM element tags.

| function App() {   return (     \<div\>       \<header\>         \<img src="assets/react-core-concepts.png" alt="Stylized atom" /\>         \<h1\>React Essentials\</h1\>         \<p\>           Fundamental React concepts you will need for almost any app you are           going to build\!         \</p\>       \</header\>       \<main\>         \<h2\>Time to get started\!\</h2\>       \</main\>     \</div\>   ); } export default App; |
| :---- |

![][image4]

The main component which imports every other components should be given to an actual DOM element via ReactDOM.createRoot:

| import ReactDOM from "react-dom/client"; import App from "./App"; import "./index.css"; const entryPoint \= document.getElementById("root"); ReactDOM.createRoot(entryPoint).render(\<App /\>); |
| :---- |

### child component

Components can refer to other components so they are combinable. In the following example, we add a Header component in the App parent component.

| function App() {   return (     \<div\>       \<Header /\>       \<main\>         \<h2\>Time to get started\!\</h2\>       \</main\>     \</div\>   ); } function Header() {   return (     \<header\>       \<img src="assets/react-core-concepts.png" alt="Stylized atom" /\>       \<h1\>React Essentials\</h1\>       \<p\>         Fundamental React concepts you will need for almost any app you are         going to build\!       \</p\>     \</header\>   ); } export default App; |
| :---- |

### dynamic properties

The content of a component can be dynamic by using curly braces. In the following example, we add a value in the content of the paragraph which is dynamically computed when rendering the Header. Similarly, images can be added. It is possible to use a ternary operator to render one value or another.

| import reactImg from "./assets/react-core-concepts.png";  const reactDesc \= \["Fundamental", "Crucial", "Core"\]; function getRandomInt(max) {   return Math.floor(Math.random() \* (max \+ 1)); } function Header() {   const randomInt \= getRandomInt(reactDesc.length \- 1);   const desc \= reactDesc\[randomInt\];    return (     \<header\>       \<img src={reactImg} alt="Stylized atom" /\>       \<h1\>React Essentials\</h1\>       \<p\>         {desc} React concepts you will need for almost any app you are going to         build\!       \</p\>       {randomInt \=== 0 ? (\<p\>Zero was selected.\</p\>) : null}     \</header\>   ); } |
| :---- |

Dynamic properties can be JSX element or array of JSX elements:

| // core concepts let coreConceptsElt \= \[\]; for (const coreConcept of CORE\_CONCEPTS) {   coreConceptsElt.push(\<CoreConcept {...coreConcept} /\>); } |
| :---- |
| ...  **\<ul\>{coreConceptsElt}\</ul\>** ... |

### Properties

Components can have properties when they are added in other components. For that we use attributes when inserting it which we can get in the props object.

| import componentImg from "./assets/components.png"; function App() {   return (     \<div\>       \<main\>         \<section id="core-concepts"\>           \<h2\>Core Concepts\</h2\>           \<ul\>             \<CoreConcept               title\="components"               description\="the code UI building block"               img\={componentImg}             /\>           \</ul\>         \</section\>       \</main\>     \</div\>   ); } function CoreConcept(props) {   return (     \<li\>       \<img src={props.img} /\>       \<h3\> {props.title} \</h3\>       \<p\> {props.description}\</p\>     \</li\>   ); } |
| :---- |

Alternatively, pass the properties via object destructuring:

| import componentImg from "./assets/components.png"; function App() {   const data \= {     title: "components",     description: "the code UI building block",     image: componentImg,   };   return (     \<div\>       \<Header /\>       \<main\>         \<section id="core-concepts"\>           \<h2\>Core Concepts\</h2\>           \<ul\>             \<CoreConcept {...data} /\>           \</ul\>         \</section\>       \</main\>     \</div\>   ); } function CoreConcept(props) {   return (     \<li\>       \<img src={props.image} /\>       \<h3\> {props.title} \</h3\>       \<p\> {props.description}\</p\>     \</li\>   ); } |
| :---- |

Destructuring in component is possible:

| function CoreConcept({image,title,description}) {   return (     \<li\>       \<img src={image} /\>       \<h3\> {title} \</h3\>       \<p\> {description}\</p\>     \</li\>   ); } |
| :---- |

One of the special properties which is always given, is the “**children**” property. This property includes any child html code in the component. For instance, the TabButton gets a paragraph html element with the text  “Components” which is given by the “**children**” property.

| ... \<TabButton\>\<p\>Components\</p\>\</TabButton\> ... |
| :---- |
| export default function TabButton(props) {   return (     \<li\>       \<button\>{**props.children**}\</button\>     \</li\>   ); }  |

it is possible to give JSX as value for a property. For instance, here, We create a Tabs component which has its buttons property set with a fragment containing three paragraphs. The children property is also a paragraph. It is another way than children property, also to pass JSX to components.

| export default function Tabs({ children, buttons }) {   return (     \<\>       \<menu\> {buttons}\</menu\>       {children}     \</\>   ); } |
| :---- |
| \<**Tabs**   **buttons**\={     \<\>       \<p\>hello 1\</p\>       \<p\>hello 2\</p\>       \<p\>hello 3\</p\>     \</\>   } \>   \<p\>Content\</p\> \</Tabs\> |

Additionally, we can pass component types and even standard component types (like div or menu) to tell the sub-component to use a dynamic type in its JSX. For instance, suppose the Tabs component has a buttonsContainer property which is the type of the parent of the buttons. We can then pass a standard menu (as string) or a custom Menu component (as dynamic value) to the Tabs component. Note that we have to use a property name that starts with a capital letter to indicate that it is a type.

| export default function Tabs({ children, buttons, ButtonsContainer }) {   return (     \<\>       \<ButtonsContainer \> {buttons}\</ButtonsContainer \>       {children}     \</\>   ); } |
| :---- |
| \<Tabs   **ButtonsContainer="menu"**   buttons={     \<\>       \<p\>hello 1\</p\>       \<p\>hello 2\</p\>       \<p\>hello 3\</p\>     \</\>   } \>   \<p\>Content\</p\> \</Tabs\> |
| \<Tabs   **ButtonsContainer={Menu}**   buttons={     \<\>       \<p\>hello 1\</p\>       \<p\>hello 2\</p\>       \<p\>hello 3\</p\>     \</\>   } \>   \<p\>Content\</p\> \</Tabs\> |

### Default property value

With the \= after the property name, we can declare a default value to it.

| export default function Tabs({ children, buttons, ButtonsContainer \= "menu" }) {   return (     \<\>       \<ButtonsContainer \> {buttons}\</ButtonsContainer \>       {children}     \</\>   ); } |
| :---- |

### Styling

It is usually a good practice to name the css files containing the styling of the component, with the name of the component. The css code will be applied for every component though. The style is **not scoped** to the component. This means that components using the same class of the css file, will use the corresponding style. The file should thus be imported in the js code:

| import "./CoreConcept.css";  export default function CoreConcept({ image, title, description }) {   return (     \<li\>       \<img src={image} /\>       \<h3\> {title} \</h3\>       \<p\> {description}\</p\>     \</li\>   ); } |
| :---- |

### Event handling

All standard React component names start with a lower case. Those are usually the default html element tag names. Some of those components have an onClick property. We can give a value to this property which should be a function:

| export default function TabButton(props) {   const onClick \= function () {     console.log("hello");   };   return (     \<li\>       \<button onClick={onClick}\>{props.children}\</button\>     \</li\>   ); } |
| :---- |

Of course, this function can be given to the component via props.

### State

If we want to update a component visualization we must use the concept of state. States are members of a Component which have a getter and a setter, and which will trigger the reevaluation of the component and its children component ui, when the setter is executed. By default, the JSX code returned by the component is never reevaluated unless a state has changed. To declare a state, we have to use a special function provided by react called **useState**. This function must be called in the main scope of the component function (not in another function, not in an if-clause, not in a for-loop, …). This function gets the default value of the member as input and returns the getter (as value, not as function) and the setter function. When the setter function is evaluated, the main function of the component is re-executed. In the following example, the label of the button is updated with a random float between 0 and 1 each time we press the button.

| import { useState } from "react";  export default function RandomTabButton() {   const \[getNumber, setNumber\] \= useState(0);   const onClick \= function () {     setNumber(Math.random());   };   return (     \<li\>       \<button onClick={onClick}\>{getNumber}\</button\>     \</li\>   ); } |
| :---- |

We can also pass a function to the setter which will have the previous value as argument and should return the new value. This is a better practice if the new value is based on the previous value because the previous state might not be the one from the getter (for instance, if you look at the example below, previousNumber is not getNumber). It is important to make a copy of the previous state value and not update it because the previous value only lives during the lambda execution.

| import { useState } from "react"; export default function RandomTabButton() {   const \[getNumber, setNumber\] \= useState(0);   const onClick \= function () {     setNumber((previousNumber) \=\> previousNumber+1);   };   return (     \<li\>       \<button onClick={onClick}\>{getNumber}\</button\>     \</li\>   ); } |
| :---- |

It is important to know that we execute a setter, this execution is scheduled on a queue.

### lifting the state up

When two components need the same state, a pattern is to lift the state to the closest parent.  
![][image5]

### CSS Classes

in react, the css class are passed to an element with property **className**, which value can also be dynamic:

| export default function TabButton({ children, onClick, isActive }) {   return (     \<li\>       \<button className={isActive ? "active" : null} onClick={onClick}\>         {children}       \</button\>     \</li\>   ); } |
| :---- |

## React Essentials \- Deep Dive

### Avoiding using JSX

It is possible to use the static method React.createElement that output jsx element:  
![][image6]

### Fragment and empty elements

Any React component must return a single element. We cannot return multiple elements. But if the main DOM element should not be rendered, we can use the React Fragment element or the empty “\<\>...\</\>” element. For instance, in this example, the div is not needed because it does not need any styling, so we can use the empty component:

| function App() {   return (     \<\>       \<header\>         \<img src="assets/react-core-concepts.png" alt="Stylized atom" /\>         \<h1\>React Essentials\</h1\>         \<p\>           Fundamental React concepts you will need for almost any app you are           going to build\!         \</p\>       \</header\>       \<main\>         \<h2\>Time to get started\!\</h2\>       \</main\>     \</\>   ); } export default App; |
| :---- |

### Forwarding props to wrapped elements

It is possible to automatically forward properties set as attributes when creating a component, to its sub-components. For instance, when we instantiate the Section component, we set the id and title attributes. The title is intercepted in the argument of the Section component, and the rest of the attributes (including the id), is gathered in this props arguments. The three dots in front tell it to gather all other non-intercepted attributes and put them in a props object, including the id. When creating the standard section component, the three dots indicate to destructure the props object to create a dynamic list of attributes to pass to the standard section sub-component.

| \<Section title="Examples" id="examples"\> ... \</Section\> |
| :---- |
| export default function Section({ title, children, **...props** }) {   return (     \<section **{...props}**\>       \<h2\>{title} \</h2\>       {children}     \</section\>   ); } |

## Styling React Components

### Vanilla CSS Styles Are NOT Scoped To Components\!

![][image7]

The main disadvantage of vanilla css, imported in the component JS code, is that the style in this css is not scoped to the component. If for instance, I declare a style for the paragraph p, any paragraph will get this style, no matter where the css file was imported.

### Styling React Apps with Inline Styles

We can add style directly to the React code by adding the style attribute. This **style** attribute expects an object as dynamic value (hence the double curly braces) which properties are the css properties. The css properties inside override the css properties from the css file.

| import logo from "../assets/logo.png"; import "./Header.css"; export default function Header() {   return (     \<header\>       \<img src={logo} alt="A canvas" /\>       \<h1\>ReactArt\</h1\>       \<p style={{ color: "yellow" }}\>          A community of artists and art-lovers.       \</p\>     \</header\>   ); } |
| :---- |

![][image8]

The problem of this technique is that we are going to copy paste the style to all components.

### Dynamic & Conditional Styling with CSS Files & CSS Classes

Alternatively, we can add css classes with the className attribute. This attribute has string as value, which is a list of css classes separated by a space.

### Scoping CSS Rules with CSS Modules

It is possible to scope css classes to a component by:

- naming the css file as \<component\>.module.css  
- import the classes object from this css file in the component  
- access the class from the classes object

| import logo from "../assets/logo.png"; import classes from "./Header.module.css";  export default function Header() {   return (     \<header\>       \<img src={logo} alt="A canvas" /\>       \<h1\>ReactArt\</h1\>       \<p className={classes.paragraph}\>         A community of artists and art-lovers.       \</p\>     \</header\>   ); } |
| :---- |

This only works with classes. Behind the screen, thanks to the “module” css file name, the vite framework will create class names based on the path of the class and assign this class the element of the component using it. The classes properties are simple string so you still pass them via props.

![][image9]

### The Styled-Component package

To install styled-component, this will update the package.json

| npm install styled-component |
| :---- |

With that, we can make style component which can be stored in a separated file:

| import { styled } from "styled-components";  const ControlContainer \= styled.div\`   display: flex;   flex-direction: column;   gap: 0.5rem;   margin-bottom: 1.5rem; \`; export default ControlContainer; |
| :---- |

Under the hood, it creates a div with a special scoped class:  
 ![][image10]

If the JS code injects conditionally a new “invalid” class name, the generated html code will contain this class too. We can mix both approaches.  
![][image11]

Alternatively to use the className property to add classes, we can conditionally add style properties to the css code in the styled component. The conditions are accessible via the props arguments in the tagged template (the string with the back-ticks). These props are accessible because the caller of component has set attributes.

| ... \<Label invalid={emailNotValid}\>Email\</Label\> ... |
| :---- |
| import { styled } from "styled-components"; const Label \= styled.label\`   display: block;   margin-bottom: 0.5rem;   font-size: 0.75rem;   font-weight: 700;   letter-spacing: 0.1em;   text-transform: uppercase;   color: **\${({ invalid }) \=\> (invalid ? "\#f87171" : "\#6b7280")}**; \`; export default Label; |

We can also make sure the style of the children components are set in the css of the styled component. for that we use the & selector which also works in media query. The following code wraps a h1 and a p, in a styled component called StyledHeader.

| import { styled } from "styled-components"; const StyledHeder \= styled.header\`   display: flex;   flex-direction: column;   align-items: center;   & h1 {     font-size: 1.5rem;   }   & p {     text-align: center;   }   @media (min-width: 768px) {     margin-bottom: 4rem;     & h1 {       font-size: 2.25rem;     }   } \`; export default function Header() {   return (     \<StyledHeder\>       \<h1\>ReactArt\</h1\>       \<p\>A community of artists and art-lovers.\</p\>     \</StyledHeder\>   ); } |
| :---- |

The & selector can also be used with pseudo selector:

| import { styled } from "styled-components"; const Button \= styled.button\`   padding: 1rem 2rem;   font-weight: 600;   text-transform: uppercase;   border-radius: 0.25rem;   color: \#1f2937;   background-color: \#f0b322;   border-radius: 6px;   border: none;   &:hover {     background-color: \#f0920e;   } \`; export default Button; |
| :---- |

## Debugging React Application

### StrictMode

This is a react component that can wrap the main component. This means that this component will always be executed twice.

| import { StrictMode } from "react"; import ReactDOM from "react-dom/client"; import App from "./App"; import "./index.css"; ReactDOM.createRoot(document.getElementById("root")).render(   \<StrictMode\>     \<App /\>   \</StrictMode\> ); |
| :---- |

## Working with Refs and Portals

### Connecting & Accessing HTML Elements via Refs

The main purpose of a ref is to access one DOM element from another. We use **useRef** to get a variable whose **current** property contains the reference to the DOM element to which we assigned this variable via the **ref** attribute. In the following example, we can access the input from a button onClick lambda.   
In other words:

- useRef() makes the common variable  
- this variable current property contains a DOM element  
- we define the DOM element that should be referred via the ref property of this element

To produce the same effect without ref, we should have two states. The two states are similar to the view-viewmodel pattern. One state has the player name in the input component; it is the viewmodel. The other state that is seen in the h2. The first player name value, is written in the second when we click on the button; the second is thus the model.

| import { useState, useRef } from "react"; export default function Player() {   const \[playerName, setPlayerName\] \= useState("unknown entity");   const playerNameInput \= useRef();    const onClicked \= function () {     setPlayerName(playerNameInput.current.value);   };   return (     \<section id="player"\>       \<h2\>Welcome {playerName}\</h2\>       \<p\>         \<input type="text" ref={playerNameInput} /\>         \<button onClick={onClicked}\>Set Name\</button\>       \</p\>     \</section\>   ); } |
| :---- |

### Storing members of components

Refs can also be used to store any value in their **current** property. This value persists after re-rendering. For instance, we can store the timer pointer when it is started and use it when it is stopped, in another function.

| import {useRef } from "react"; export default TimeChallenge \= function ({ title, targetTime }) {   const timer \= useRef();    function handleStart() {     timer.current \= setTimeout(() \=\> {       setTimeExpired(true);     }, 1000 \* targetTime);     setTimerStarted(true);   }   function handleStop() {     clearTimeout(timer.current);     setTimerStarted(false);   } ... }; |
| :---- |

### Forwarding Refs to Custom Components

As any other properties, this ref value can be passed to a custom component so that this component lets its parent access some inner component.

| import {useRef } from "react"; import ResultModal from "./ResultModal"; export default TimeChallenge \= function ({ title, targetTime }) {   const dialog \= useRef();   ...   return (     \<\>       \<ResultModal ref={dialog} targetTime={targetTime} result="lost" /\>       ...     \</\>   ); }; |
| :---- |
| export default function ResultModal({ **ref**, result, targetTime }) {   return (     \<dialog **ref={ref}** className="result-modal"\>       ...     \</dialog\>   ); } |

Before react 19, this was not possible, so we were using **forwardRef** function. From react 19, we can simply pass ref at props parameter.

###  Refs vs State Values

1. The main difference with states, is that ref is only accessible after rendering the react component. You cannot use the ref.current in the react component function body because at the rendering time, the ref is not set yet. Indeed the connection with the ref attribute is not set yet.

2. Ref does not trigger the re-rendering of a component. If the component should be re-render at a point, it must have a state. State are used for values that have direct ui impacts. Ref are used for behind-the-scene impacts.

3. Refs, like States, are not reinitialized after re-rendering. They keep their previous value when re-rendering occurs.

### Exposing Component APIs via the useImperativeHandle Hook

This hook is used to expose methods from a component to its parent. It works by making a ref in the parent, pass it via props to a children, and use useImperativeHandle with it. The first argument of the useImperativeHandle must be a ref and the second argument is a js object with methods exposed to the ref.current variable. With this way, the parent can access methods of the children.  
In other words, the “ref” variable is used as a common pointer for the parent and the child. It is made with useRef(). The child use useImperativeHandle to define what this pointer can provide.

For instance, in the following example, we make a “dialog” ref, in the parent, which is passed to the ResultModal. In the parent, a lambda accesses the “dialog” ref open() method, which is defined in the useImperativeHandle js object. 

| import { useState, useRef } from "react"; import ResultModal from "./ResultModal"; export default TimeChallenge \= function ({ title, targetTime }) {   ...   const dialog \= useRef();    function handleStart() {     timer.current \= setTimeout(() \=\> {       setTimeExpired(true);       dialog.current.open();     }, 1000 \* targetTime);     setTimerStarted(true);   }   return (     \<\>       \<ResultModal impl={dialog} targetTime={targetTime} result="lost" /\>       ...     \</\>   ); };  |
| :---- |
| import { **useImperativeHandle**, useRef } from "react"; export default function ResultModal({ impl, result, targetTime }) {   const dialog \= useRef();   **useImperativeHandle(impl, () \=\> {     return {       open() {         dialog.current.showModal();       },     };   });**    return (     \<dialog **ref={dialog}** className="result-modal"\>       ...     \</dialog\>   ); } |

## React’s Context API & useReducer

### Understanding Prop Drilling

So far, when a state is shared among multiple components, we tend to **lift the state up** to the nearest parent component. For instance if a shopping cart is displayed on the Cart and updated in the Product component, we should manage the state of this cart in the App and provide the state via props to the two branches of the component tree.

Prop drilling is the fact of passing shared data through multiple components layers, although most components do not need this data. The problem with that is that the intermediate components do not need this state but they need to be used with this state. Therefore it makes reusability more difficult.

![][image12]

One solution of this problem is to instantiate the component that needs the state directly in the component that manages it, and then pass this instantiated component, as a child (in the children props), to the intermediate component so that it renders it as a child without passing the state.   
In the upper example, we could move the creation of Product components in the App component and pass them as children to the Shop component.  
The problem of this solution is that the App component would get a lot of components making all other intermediate components, simple wrappers. 

### React’s Context API

The idea of the context is to wrap the entire part of the tree with a special Context component and to let the component which needs to read and write in the state, accessing the method of the state. When the Context changes, the components that use this Context are re-rendered.

![][image13]

**Creation:**

A context is usually placed in a store folder and it offers a component made with createContext react function. The created context is a component hence its upper case at the start of its name. The argument to createContext is the initial value of the state and some method signature to update it. This default value is used as a state, if the component that reads or writes the state is not used in a tree wrapped by the context component.

| import { createContext } from "react"; const CartContext \= createContext({   items: \[\],   addItemToCart: () \=\> {},   updateItemInCart: () \=\> {}, }); export default CartContext; |
| :---- |

**Usage in main component**

Once exported, we can use it as a wrapper component, in a component which children need the state. Before React 19, we would have to use CartContext.Provider. We must also give a **value** attribute to this wrapping component. This value is the state with its update methods created in the main component. The difference with the default value when creating the Context, is that this value is provided to the children component, in the tree wrapped by the Context component.

| ... import CartContext from "./store/shopping-cart-context"; function App() {  const \[shoppingCart, setShoppingCart\] \= useState({     items: \[\],   });  const handleAddItemToCart \= ...  const handleUpdateCartItemQuantity= ...  const cartContextValue \= {     items: shoppingCart.items,     addItemToCart: handleAddItemToCart,     updateItemInCart: handleUpdateCartItemQuantity,   };   return (     \<CartContext value={cartContextValue}\>       \<Header         ...       /\>       \<Shop\>         ...       \</Shop\>     \</CartContext\>   ); } |
| :---- |

**reading and writing in the Context**

This wrapper ensures that we can use the state in the components in the tree. If we want to read or write the state in the Context, we need to import the context and also import the **use** or **useContext** react hook. Both hooks take the context component as argument. The main two differences between those hooks is that the use hook is accessible from React 19 and that it can be used in if-clause. The returned value of use or useContext, is the Context value as given in the wrapping Context component. In our example, the **items and the updateItemInCart** property is in the Context value. Therefore they can be used.

| import { use } from "react"; import CartContext from "../store/shopping-cart-context"; export default function Cart() {   const {items, updateItemInCart} \= use(CartContext);   ... } |
| :---- |

In certain old React applications, there is another way of accessing the context value. We can wrap the rendered consuming component with the CartContext.Consumer component. This component should get a function as child, which has the Context value as argument, and should output this wrapped consuming component.

| import CartContext from "../store/shopping-cart-context"; export default function Cart() {   return (   \<CartContext.Consumer\>   {(cartContextValue) \=\>     {     ...     return (...);     }   }   \</CartContext.Consumer\>   ) } |
| :---- |

**Managing state and context in the same “ContextProvider” component**

In the above, we suppose that the main component wrapping the tree with the Context component, is managing the state. It offers the value and the setter of the state. An alternative to that is to let the Context component manage the state.  
To make such a Context Provider component, we must:

- create and export a new component which name ends by ContextProvider. This new component should have children props.  
- declare and export the Context in outside of this ContextProvider component function   
- declare the state in the ContextProvider component function  
- declare some method for the Context value and make the context value.  
- return the Context(.Provider) as main component and the children inside.

For instance, we can make a CartContextProvider, managing the state the context:

| import { createContext, useState } from "react"; export const CartContext \= createContext({   items: \[\],   addItemToCart: () \=\> {},   updateItemInCart: () \=\> {}, }); export default function CartContexProvider({ children }) {   const \[shoppingCart, setShoppingCart\] \= useState({     items: \[\],   });   function handleAddItemToCart(id) {...}   function handleUpdateCartItemQuantity(productId, amount) {...}   const cartContextValue \= {     items: shoppingCart.items,     addItemToCart: handleAddItemToCart,     updateItemInCart: handleUpdateCartItemQuantity,   };   return \<CartContext value={cartContextValue}\>{children}\</CartContext\>; } |
| :---- |

The component using this ContextProvider can then simply wraps its children consuming the Context: 

| import Header from "./components/Header"; import Shop from "./components/Shop"; import CartContextProvider from "./store/shopping-cart-context"; function App() {   return (     \<CartContextProvider\>       \<Header /\>       \<Shop /\>     \</CartContextProvider\>   ); } export default App;  |
| :---- |

### useReducer hook

**useReducer is an alternative to useState** useful when the state of the application depends on the previous state. To use it:

- import **useReducer** from react library.  
- use **useReducer**, with a **Reducer function** and an initial value of the state like in use state. This Reducer function will handle the update of the state based on the previous state. useReducer returns the **state** and the **Dispatch** function.  
- Implement the Reducer function. This reducer function gets the previous state and the **action** as a parameter. The action contains any argument we want to pass.  
- When implementing the handling function, we use the **Dispatch** function in the body of the handling function, with the action. The action could contain a type and a payload to identify how the Reducer function should update the state.

| import { createContext, useReducer } from "react"; export const CartContext \= createContext({   items: \[\],   addItemToCart: () \=\> {},   updateItemInCart: () \=\> {}, }); function shoppingCartReducer(state, action) {   if (action.type \=== "ADD\_ITEM") {...};   } else if (action.type \=== "UPDATE\_ITEM") {...}   return state; } export default function CartContexProvider({ children }) {   const \[shoppingCartState, shoppingCartDispatch\] \= useReducer(     shoppingCartReducer,     {       items: \[\],     }   );   function handleAddItemToCart(id) {     shoppingCartDispatch({ type: "ADD\_ITEM", payload: id });   }   function handleUpdateCartItemQuantity(productId, amount) {     shoppingCartDispatch({       type: "UPDATE\_ITEM",       payload: { productId, amount },     });   }   const cartContextValue \= {     items: shoppingCartState.items,     addItemToCart: handleAddItemToCart,     updateItemInCart: handleUpdateCartItemQuantity,   };   return \<CartContext value={cartContextValue}\>{children}\</CartContext\>; } |
| :---- |

## Handling side effects & working with useEffect hook

UseEffect hook is used to schedule tasks that have effects on the UI. The first rendering cycle triggers the task, and another cycle is triggered after the task is completed because of a state change.   
For instance, a task could be fetching the user coordinates to trigger some different rendering. As this task is asynchronous (we will get a coordinate after a moment, triggering a call-back function), we need to render the page again after the task is finished, but not during the current execution when this task is scheduled.

### Using useEffect for Handling (Some) Side Effects

We can use useEffect to execute a function once after rendering the component. For that this hook takes two parameters. A function to be executed and a list of dependencies. If this list is empty, the function will be executed once, while if it is not given, the function is executed each time after the component is rendered.

For instance, here we set a state with the use of the user coordinate. As the dependency list is empty, the function is triggered once. 

| import { useRef, useState, useEffect } from "react"; import { sortPlacesByDistance } from "./loc.js"; function App() {   const \[availablePlaces, setAvailablePlaces\] \= useState(\[\]);   useEffect(() \=\> {     navigator.geolocation.getCurrentPosition((position) \=\> {       const sortedPlaces \= sortPlacesByDistance(         AVAILABLE\_PLACES,         position.coords.latitude,         position.coords.longitude       );       setAvailablePlaces(sortedPlaces);     });   }, \[\]);   ... } export default App;  |
| :---- |

Another use case of useEffect is when rendering a modal. If we pass an open props to the modal component, we can control, after it has rendered, if it should be closed or opened.

| import { useEffect, useRef } from "react"; import { createPortal } from "react-dom"; function Modal({ open, children }) {   const dialog \= useRef();   useEffect(() \=\> {     if (open) dialog.current.showModal();     else dialog.current.close();   }, \[open\]);   return createPortal(     \<dialog className="modal" ref={dialog}\>       {children}     \</dialog\>,     document.getElementById("modal")   ); } export default Modal; |
| :---- |

it is important to understand that useEffect execution is only triggered depending on the dependency list. If the list is not given, the function is executed each time after the component body is executed. If the list is empty, it will be executed if the component is installed in the DOM. To illustrate that, the following code simply increments an integer starting at zero. In the log, we can see that the Header body is executed, but that the effect function is only executed once, because the Header does not change.  
A way to force the re-installation of the component, and thus the execution of the effect function, is to give the key attribute to the component. If this key changes, the DOM changes and so the effect function is reexecuted.

| import { useState, useEffect } from "react"; function App() {   const \[index, setIndex\] \= useState(0);   return (     \<\>       \<Header /\>       \<button         onClick={() \=\> {           setIndex((prev) \=\> prev \+ 1);         }}       \>         {"Click Me"}       \</button\>       \<h2\>{index}\</h2\>     \</\>   ); } function Header() {   console.log("Header body");   useEffect(() \=\> {     console.log("Header Effect");   }, \[\]);   return \<header\>\</header\>; } export default App; |
| :---- |

### useEffect dependencies

The dependencies array is the second argument of useEffect. If one of these values changes, the function of useEffect is re-executed. For instance, above, if the open props changes, we need to re-execute the useEffect function to open or close the Modal component.  
The meaning of “changes” is defined by the \===operator, so we have to be very careful with what we put in this array. For instance two functions are equal if they are the same pointer.

### useEffect clean up function

useEffect function can return a function, and this function will be executed before the next useEffect function is executed or before the component is removed from the DOM.

For instance, we can set a timer in the useEffect function, which removes this component after 3 sec. As the timer should be stopped whenever the component is removed, we should stop it in the clean up function of useEffect.

| import { useEffect } from "react"; export default function DeleteConfirmation({ onConfirm, onCancel }) {   useEffect(() \=\> {     const timer \= setTimeout(() \=\> {       onConfirm();     }, 3000);     return () \=\> {       clearTimeout(timer);     };   }, \[\]);   ... } |
| :---- |

Another interesting use-case of useEffect with its clean-up function, is when the component should re-render at a certain frequency. The re-rendering is forced by a state, and the frequency is made with setInterval. This function executes a function every X ms. In this situation, we can use useEffect to start the interval which will update the component, until it is removed from the DOM causing the clean-up function to be executed.

| import { useEffect, useState } from "react"; export default ProgressBar \= function ({ max }) {   const \[remainingTime, setRemainingTime\] \= useState(max);   useEffect(() \=\> {     const timer \= setInterval(() \=\> {       setRemainingTime((previousTime) \=\> previousTime \- 10);     }, 10);     return () \=\> {       clearInterval(timer);     };   }, \[\]);   return \<progress value={remainingTime} max={max} /\>; }; |
| :---- |

### useEffect not needed

If the data can be obtained directly at the first rendering, we do not need useEffect. For instance, if we store some data in the local storage (**localStorage.getItem and .setItem**), this data is not asynchronous so we can get and store it without a second pass of the rendering caused by useEffect.

### useCallback

useCallback takes a function and a dependency list as parameters. It returns the function passed, and makes sure that this function is stored and never made again for this component, unless one of the dependencies changes. If the list is empty, the function is recreated every time the component is re-rendered  
If the function uses a state setter, it is not useful to set it as dependency, because React guarantees that the setter is never recreated.

## A look behind the scene of React and optimization techniques

### React Builds A Component Tree / How React Works Behind The Scenes

Rendering a component means executing the component function. The children components are rendered when the parent is rendered, in the order of appearance in the JSX returned by the parent. React makes a tree of components.

When a state is changed, the underlying tree is re-rendered. The parent and above are not re-rendered.

Rendering does not mean that the states are recreated. To recreate a state, the component needs to be dismounted and remounted on the DOM. In the following example, each time we click on the button, the state of the App component (a simple integer) is changed and thus the App is re-rendered. The Header component is re-rendered too, but as the state is not recreated, the “headerIndex” state is not recreated so it does not change. A way to force re-mounting the Header, is to add the “key” attribute to the Header with the value of the “index” state.

| import { useState } from "react"; function App() {   const \[index, setIndex\] \= useState(0);   return (     \<\>       \<Header index={index} /\>       \<button         onClick={() \=\> {           setIndex((prev) \=\> prev \+ 1);         }}       \>         {"Click Me"}       \</button\>       \<h2\>{index}\</h2\>     \</\>   ); } function Header({ index }) {   const \[headerIndex, setHeaderIndex\] \= useState(index);   return (     \<header\>       \<h2\>Header:{headerIndex}\</h2\>     \</header\>   ); } export default App; |
| :---- |

### Avoiding Component Function Executions with memo()

memo() is a react hook that gets the component function as argument, and returns the old JSX of the wrap component (so the result of the execution of the component function), if the props did not change (using the \===operator). If one of them changed, then the component function is re-executed and the JSX is returned. It is not performant to use memo() on every component function, because React has to evaluate each component props, so it costs performance. It is useful if the component is high in the tree and has few props.

For instance, in the following example, the Header component is only re-rendered if the memoIndex state change. We clearly see this because if memoIndex state is changed via the “Memo” button, the Header random number is re-generated. If we remove the memo, the number is re-generated on the “normal” button clicked, too, because of a change of state (here the state “index”) of the parent.

| import { useState, memo } from "react"; function App() {   const \[index, setIndex\] \= useState(0);   const \[memoIndex, setMemoIndex\] \= useState(0);   return (     \<\>       \<Header value={memoIndex} /\>       \<button         onClick={() \=\> {           setIndex((prev) \=\> prev \+ 1);         }}       \>         {"Normal"}       \</button\>       \<h2\>normal:{index}\</h2\>       \<button         onClick={() \=\> {           setMemoIndex((prev) \=\> prev \+ 1);         }}       \>         {"Memo"}       \</button\>       \<h2\>memo:{memoIndex}\</h2\>     \</\>   ); } const Header \= memo(function ({ value }) {   return \<header\>Header:{Math.random()}\</header\>; }); export default App; |
| :---- |

### Understanding the useMemo() Hook

useMemo() takes a function without argument, and a list of dependencies as input and returns the output of the memorized function. The idea of useMemo is to cash the value returned by the function, and to re-evaluate the function if a dependency changed. Of course, as the \===operator is used for every dependency, there is a performance cost. If the execution of the function is expensive compared to the comparison of its dependencies, it is worth using useMemo().

### Introducing the React Compiler

The compiler automatically optimizes your React application by handling memoization for you, eliminating the need for manual useMemo, useCallback, and React.memo.

### React Uses A Virtual DOM \- Time To Explore It\!

React works with a virtual DOM. It creates and compares the virtual DOM snapshots to find out which parts of the rendered UI need to be updated:

1. First it recreates the Tree but only the parts that are impacted by changes of state are re-evaluated.  
2. Second, it creates the virtual snapshot of the new HTML code.  
3. Then it compares virtually the new virtual snapshot with the old one which it had stored from the previous iteration.  
4. Finally it applies the changes to the real DOM.

### Why Keys Matter When Managing State\!

states are scoped to a component. If two components of the same type are mounted, two independent states are created.  
This state is assigned to a component instance based on its depth in the DOM, its position among siblings, its key property and its type.   
To illustrate that let’s make a button that pops buttons. Each added button is added before the others. When clicking those generated buttons, the text changes. As we can see, the “text” state of the generated buttons, is linked to the position of the button in the list items. So if the second is clicked, and then we click on the generating button, the second generated is marked as “clicked” while it should be the third. This is caused by the fact that react assigns the state of a component based on its position among siblings and the key. As the key is not used, it only uses this position, therefore, when we change the state of the second, that’s the second that gets the state update.

| import { useState } from "react"; function App() {   const \[array, setArray\] \= useState(\[\]);   return (     \<\>       \<button         onClick={() \=\> {           setArray((prev) \=\> \[{ text: "unclicked" }, ...prev\]);         }}       \>         {"Click Me"}       \</button\>       \<ol\>         {array.map((item) \=\> (           \<Item initialText={item.text} /\>         ))}       \</ol\>     \</\>   ); } function Item({ initialText }) {   const \[text, setText\] \= useState(initialText);   return (     \<li\>       \<button         onClick={() \=\>           setText((prev) \=\> (prev \=== "unclicked" ? "clicked" : "unclicked"))         }       \>         {text}       \</button\>     \</li\>   ); } export default App; |
| :---- |

To counter this, we use the key property with a unique id, which cannot be the index in the array of “unclicked” because the state would be assigned again based on the position.

| import { useState } from "react"; function App() {   const \[array, setArray\] \= useState(\[\]);   return (     \<\>       \<button         onClick={() \=\> {           setArray((prev) \=\> \[             { text: "unclicked", id: Math.random() },             ...prev,           \]);         }}       \>         {"Click Me"}       \</button\>       \<ol\>         {array.map((item) \=\> (           \<Item key={item.id} initialText={item.text} /\>         ))}       \</ol\>     \</\>   ); } function Item({ initialText }) {   const \[text, setText\] \= useState(initialText);   return (     \<li\>       \<button         onClick={() \=\>           setText((prev) \=\> (prev \=== "unclicked" ? "clicked" : "unclicked"))         }       \>         {text}       \</button\>     \</li\>   ); } export default App; |
| :---- |

The other advantage of using this key, is that React compares the old and new DOM based on the key too, it understands that only the first element changes.

### State Scheduling & Batching

States updates are scheduled on a queue. Therefore, the new state is not accessible directly after the use of the state setter. The order of the schedule is the order of the usage.

If multiple state updates are scheduled one after another, they are executed together, and only the final state value is used to re-render the tree. This is called state batching.

## Sending Http request

### Sending HTTP Requests via useEffect

As getting data means treating an asynchronous action, we need to use **useEffect** with fetch. **fetch**() returns a Promise so we have to use **then**() to get the response inside. **json**() also returns a promise and provides the body of the response. Once the body is retrieved, we can use the setter of the state to re-render the component. It is important to not use fetch(...).then(... setState) in the body of the component, but in useEffect. Indeed, if we use fetch() in the body, combined with setState, it creates an infinite loop.

In the following example, we retrieve the “places” from the server.

| import { useState, useEffect } from "react"; import Places from "./Places.jsx"; export default function AvailablePlaces({ onSelectPlace }) {   const \[availablePlaces, setAvailablePlaces\] \= useState(\[\]);   useEffect(() \=\> {     fetch("https\://localhost:7068/Places")       .then((response) \=\> {         return response.json();       })       .then((places) \=\> {         setAvailablePlaces(places);       });   }, \[\]);   return (     \<Places       title="Available Places"       places={availablePlaces}       fallbackText="No places available."       onSelectPlace={onSelectPlace}     /\>   ); } |
| :---- |

### CORS

When developing a local FE (hosted by a Web-Server) and BE (hosted by a BE-server), there is a default policy CORS (cross-origin-resource-sharing) that blocks any response asked by any JS from any web-site (a web-server). This is security from the browser. Without that, any web-server could give a JS code, asking for any data to any BE-server. The browser blocks by default any response if the web-server is not trusted by the response sent by the BE-server.

That’s why it is up to the BE-server to give a special response header indicating which url of the Web-Server is authorized to serve JS to connect to the API of this BE-server. The browser checks then if the BE-server authorized the Web-server.

![][image14]

### Using async/await

Instead of using the Promise then() method, we can use **async/await** logic. The lambda function in the useEffect, cannot be async so we must declare an async function which we execute in the useEffect without the await keyword in front. This means that this async function will be executed in another event loop.

| import { useState, useEffect } from "react"; import Places from "./Places.jsx"; export default function AvailablePlaces({ onSelectPlace }) {  const \[availablePlaces, setAvailablePlaces\] \= useState(\[\]);    async function fetchPlace() {     const response \= await fetch("https\://localhost:7068/Places");     const places \= await response.json();     setAvailablePlaces(places);   }   useEffect(() \=\> {     fetchPlace();   }, \[\]);   return (     \<Places       title="Available Places"       places={availablePlaces}       fallbackText="No places available."       onSelectPlace={onSelectPlace}     /\>   ); } |
| :---- |

A POST request is very similar i.e. we call fetch function with a POST method and a body. The call itself is usually triggered in click event which is not awaited, but the change of state is synchronized with the response.

| export async function addEvent(event) {   const url \= "http\://localhost:3000/events";   const response \= fetch(url, {     method: "POST",     body: JSON.stringify(event),     headers: { "Content-Type": "application/json" },   });   if (\!response.ok) {     const error \= new Error("An error occurred while adding an events");     error.code \= response.status;     error.info \= await response.json();     throw error;   }   const newEvent \= await response.json();   return newEvent; } |
| :---- |

### Handling loading state

While the data is loading from the server, we can put an alternative text. This text is controlled by the isLoading state which is set to true when the fetching is started, and false when it is done.

| import { useState, useEffect } from "react"; import Places from "./Places.jsx"; export default function AvailablePlaces({ onSelectPlace }) {   const \[availablePlaces, setAvailablePlaces\] \= useState(\[\]);   const \[isLoading, setIsLoading\] \= useState(false);   async function fetchPlace() {     const response \= await fetch("https\://localhost:7068/Places");     const places \= await response.json();     setAvailablePlaces(places);     setIsLoading(false);   }   useEffect(() \=\> {     setIsLoading(true);     fetchPlace();   }, \[\]);   return (     \<Places       title="Available Places"       places={availablePlaces}       isLoading={isLoading}       loadingText="loading data ..."       fallbackText="No places available."       onSelectPlace={onSelectPlace}     /\>   ); } |
| :---- |

### Handing http errors

The http request may fail for two reasons. Either the connection is not established, and the an exception is thrown by the fetch function, either the back-end answers but the status code is not 200\. Therefore, for those two cases, we should handle it with a try-catch clause.

In the following example, the error state is set to an object if there is any exception when retrieving the data or if the status code is not 200\.

| import { useState, useEffect } from "react"; import Places from "./Places.jsx"; import Error from "./Error.jsx"; export default function AvailablePlaces({ onSelectPlace }) {   const \[availablePlaces, setAvailablePlaces\] \= useState(\[\]);   const \[isLoading, setIsLoading\] \= useState(false);   const \[error, setError\] \= useState(null);   async function fetchPlace() {     try {       const response \= await fetch("https\://localhost:7068/Placessss");       if (\!response.ok) {         throw new Error("Failed to fetch places");       }       const places \= await response.json();       setAvailablePlaces(places);     } catch (error) {       console.log("failed", error);       setError({ message: error.message \|\| "Failed to fetch places" });     }     setIsLoading(false);   }   useEffect(() \=\> {     setIsLoading(true);     fetchPlace();   }, \[\]);   if (error) {     console.log("rendering", error);     return \<Error title="An error occurred" message={error.message} /\>;   }   return (     \<Places       title="Available Places"       places={availablePlaces}       isLoading={isLoading}       loadingText="loading data ..."       fallbackText="No places available."       onSelectPlace={onSelectPlace}     /\>   ); } |
| :---- |

### Using http request body and using request method

The body is available for DELETE, POST and PUT requests. By default, the fetch function uses the GET method which does not support a body. To change this method, we must define a RequestInit object which has a **method**, a **body** and a **headers** property. The body must be a string so we must use **JSON.stringify**. The header indicates to the backend, the format with content-type header.

In the following example we can see the difference between the GET and the PUT case.

| export async function fetchAvailablePlaces() {   const response \= await fetch("https\://localhost:7068/Places");   if (\!response.ok) {     throw new Error("Failed to fetch places");   }   const places \= await response.json();   return places; } export async function updateUserPlaces(ids) {   const response \= await fetch("https\://localhost:7068/Places/user", {     method: "PUT",     body: JSON.stringify({ ids: \[...ids\] }),     headers: { "Content-Type": "application/json" },   });   if (\!response.ok) {     throw new Error("Failed to set user places");   } } |
| :---- |

## Building Custom React Hooks

### Rules of hooks

1. Only call hooks inside of component functions or inside other hooks. This means that the call to the hook should be inside the body of the component function.  
   

![][image15]

2. Only call hooks on the top level. Hook calls cannot be in an if-clause or loop. They cannot be called conditionally. They cannot be called in a callback function.

![][image16]

### Creating custom hooks

Custom hook functions must start with **use**\*. it is not only a convention but it is rather used to check if the first rule is followed.  
The state managed in a custom hook, is still belonging to the component calling the custom hook.

For instance, we could make a custom hook which fetches data from a **fetchAsyncFunction**. Note that some state getters and setters are returned.

| import { useEffect, useState } from "react"; export default function useFetch(fetchAsyncFunction, initialValue) {   const \[isFetching, setIsFetching\] \= useState(false);   const \[error, setError\] \= useState(null);   const \[fetchedData, setFetchedData\] \= useState(initialValue);   useEffect(() \=\> {     async function fetchData() {       setIsFetching(true);       try {         const initialUserPlaces \= await fetchAsyncFunction();         setFetchedData(initialUserPlaces);       } catch (error) {         setError({           message: error.message \|\| "error fetching data",         });       }       setIsFetching(false);     }     fetchData();   }, \[fetchAsyncFunction\]);   return {     error,     isFetching,     fetchedData,     setFetchedData,   }; } |
| :---- |

## Deploying React Apps

![][image17]

### Lazy loading

When serving an app from a web-server, the JS code could theoretically be served in one big file. This is not efficient because not the entire code is useful at any moment of the user usage of the web app.

The imports can be decoupled from the global js code with lazy loading. 

For component imports, instead of importing the component, with the **import** keyword, we use the **import()** function which returns a promise. The call to this function must be wrapped in a lambda which is given to the **lazy()** React function, which returns the component. The component usage must be wrapped by the **Suspense** React component whose fallback property is the alternative component while the main imported component is being fetched.

| // import BlogPage from './pages/Blog'; const BlogPage \= lazy(() \=\> import("./pages/Blog")); ... function App() {   return \<\>     ...     \<Suspense fallback={\<p\>Loading...\</p\>}\>       \<BlogPage /\>     \</Suspense\>     ...   \</\> } |
| :---- |

For imported function, we use the **import**() function again, which returns a promise with the **module** containing the function. It is probably good to use useEffect to handle the effect of the function (I did not try…)

| // import loader from './pages/Blog'; ... function App() {   ...   import("./pages/Blog").then((module) \=\> module.loader())   ...   return \<\>     ...   \</\> } |
| :---- |

### Building the App

a Web-server will serve the App to browsers. This browser does not handle JSX or TSX, so it must be transformed to JS code before uploading it to the Web-Server. With a Vite-base React project there is a build script which can be executed with 

| npm run build |
| :---- |

This creates a build folder containing the web-app for the web-server.

### Deployment

use firebase from Google to have a web-server. This is a static web-server. Create a project, add a web-application. The video of the course explains it correctly.

## Tanstack Query

### Installing

Tanstack query is a react library for making http requests. It avoids some boiler plates needed with the traditional useState, and useEffect functions. We install it with:

| npm install @tanstack/react-query |
| :---- |

### Making a http GET request

The Tanstack library offers a **useQuery** hook which handles the useEffect and useState boiler plate. This hook should get an **async** function in its object **queryFn** property. This hook only works for GET requests (we can use POST requests only if it does not change the state of the back-end). This function should return a Promise with the fetched data inside and thus, it should use the **fetch**() function (it should use any library that makes http request). This hooks returns an object with 

- the optional fetched **data**,   
- the optional **error** (the exception which could be thrown by the **queryFn** function),   
- the **isPending** boolean indicating that the request did not return yet (true). It indicates that the data is not there yet. It does not mean that the request was sent and did not return. For that case, there is the **isLoading** property.  
- the **isError** boolean indicating if the error is filled.

The App that uses Tanstack, must be wrapped around a context provider (**QueryClientProvider**) with a client (**QueryClient**).

| import { QueryClientProvider, QueryClient } from "@tanstack/react-query"; ... const queryClient \= new QueryClient(); function App() {   return (     \<QueryClientProvider client={queryClient}\>       ...     \</QueryClientProvider\>   ); } |
| :---- |
| import { **useQuery** } from "@tanstack/react-query"; import { **fetchEvents** } from "../../util/http.js"; ... export default function NewEventsSection() {   const { **data**, **isPending**, **isError**, **error** } \= **useQuery**({     queryKey: \["events"\],     **queryFn**: **fetchEvents**,   });   ... } |
| export async function fetchEvents() {   const response \= await **fetch**("http\://localhost:3000/events");   if (\!response.ok) {     const error \= new Error("An error occurred while fetching the events");     error.code \= response.status;     error.info \= await response.json();     throw error;   }   const { events } \= await response.json();   return events; |

The useQuery is a React hook so it must be in the body of the component. The queryKey is a list of keys which are used to manage the cache (see next chapter).

### Using the caching feature

Tanstack keeps a cache of the data received. The cache is keyed with the queryKey parameter. By default the cache is considered fresh for 0 second, and the cache is kept for 5 minutes. The option **stateTime** and **gcTime** allows you to change this default.

If we change the **staleTime** to 5 seconds, it means the data from the http request is considered fresh for 5 seconds and thus no network call is made during those 5 seconds after the initial call with the same queryKey. After that time, the data can still be used in the component while waiting for the server to answer.

After the **gcTime,** the date is cleaned up.

![][image18]

The **queryKey** values are used to know which cache to use. Any parameter to the request must be passed in the key (like query parameter or header parameter).

### Using the queryKey in queryFn

useQuery always passes by default an **object** to the queryFn. This object contains the querykey therefore, we can use this queryKey to find possible parameters.

| ... export default function NewEventsSection() {   const { data, isPending, isError, error } \= useQuery({     queryKey: \["events", 2\],     queryFn: (obj) \=\> fetchEvents(obj, null, obj.queryKey\[1\]),   });   ... } |
| :---- |

### Aborting request

useQuery always passes by default an **object** to the queryFn. So it is advised to accept this object by default, before adding any other parameter to this function. For instance, if we want to use a searchTerm in other calls, we should add it after this object.

In this object, we have access to a **signal** property which can be used by the browser to abort the request.

| import { useQuery } from "@tanstack/react-query"; import { fetchEvents } from "../../util/http.js"; ... export default function NewEventsSection() {   const { data, isPending, isError, error } \= useQuery({     queryKey: \["events"\],     queryFn: fetchEvents,   });   ... } |
| :---- |
| export async function **fetchEvents**(**{ signal }**, searchTerm) {   let url \= "http\://localhost:3000/events";   if (searchTerm) {     url \+= \`?search=\${searchTerm}\`;   }   const response \= await fetch(url, **{ signal }**);   if (\!response.ok) {     const error \= new Error("An error occurred while fetching the events");     error.code \= response.status;     error.info \= await response.json();     throw error;   }   const { events } \= await response.json();   return events; } |

### Disabling request

In certain situations, we want that the request is not sent unless a certain value is given. For instance, we do not want to send a search request if a search term is not given. The **enabled** option in useQuery allows to enable or disable a query to be sent. **isPending** is then true because the data is not there. There is a **isLoading** which indicates better the situation when the request was sent but did not return yet.

| ... export default function FindEventSection() {   const searchElement \= useRef();   const \[searchTerm, setSearchTerm\] \= useState();   const { data, isLoading, isError, error } \= useQuery({     queryKey: \["events", searchTerm\],     queryFn: (obj) \=\> fetchEvents(obj, searchTerm),     enabled: searchTerm \!== undefined,   });   function handleSubmit(event) {     event.preventDefault();     setSearchTerm(searchElement.current.value);   } ... } |
| :---- |

### 

### Making a http POST request

useQuery is only made for GET requests i.e. requests that do not modify the state of the backend and that return values to display. POST (which changes the state of the backend) uses **useMutation**. useMutation does not send the POST request when rendering the component. Instead, it offers a **mutate** function which can be used in a user event (like the click event) to trigger the call. This trigger will re-render the component and set **isPending** to true, and on return, **isError** and **error** might be filled. Again, an async function must be given in the **mutationFn** parameter.

Another parameter is the **onSuccess** function. This function is only triggered after the POST request is successful. In this function, it is a good idea to invalidate the cache of certain queries. To do that, we must use the **queryClient.invalidateQueries** function with the queryKey that we want to invalidate. Any cache which keys match this mask of keys, will be invalidated. For instance, any key starting with “events” will be invalidated. If **exact** is set to true, the mask should match exactly. This construction means that the **QueryClient** instance is shared between all queries.

| import { QueryClientProvider, QueryClient } from "@tanstack/react-query"; import { queryClient } from "./util/http.js"; ... function App() {   return (     \<QueryClientProvider client={queryClient}\>       ...     \</QueryClientProvider\>   ); } |
| :---- |
|  import { **useMutation** } from "@tanstack/react-query"; ... export default function NewEvent() {   const { **mutate**, **isPending**, **isError**, **error** } \= **useMutation**({     **mutationFn**: addEvent,     **onSuccess**: () \=\> {       **queryClient.invalidateQueries**({ queryKey: \["events"\], exact: false });       navigate("/events");     },   });   function handleSubmit(formData) {     **mutate**({ event: formData });   }   ... } |

**mutate** takes only one argument which it passes to the **mutationFn**. This means that if we want to pass multiple values, we have to bundle them in one object.

| export async function updateEvent({ id, updatedEvent }) {   const url \= \`http\://localhost:3000/events/\${id}\`;   const response \= await fetch(url, {     method: "PUT",     body: JSON.stringify(updatedEvent),     headers: { "Content-Type": "application/json" },   });   if (\!response.ok) {     const error \= new Error(       \`An error occurred while updating the event with id \${id}\`     );     error.code \= response.status;     error.info \= await response.json();     throw error;   }   return; } |
| :---- |
| ... export default function EditEvent() {   const navigate \= useNavigate();   const { id } \= useParams();   const { mutate, isPending: isEditPending } \= useMutation({     **mutationFn**: updateEvent,     onSuccess: () \=\> {       queryClient.invalidateQueries({ queryKey: \["events"\] });       handleClose();     },   });   function handleSubmit(formData) {     **mutate**(**{ id, updatedEvent: { event: formData }** });   }   ... } |

### 

### Disabling Automatic Refetching After Invalidations

When the mutate function is called, the current component which is using useMutation, is re-rendered. This means that if the component is also querying data that it has deleted, the server will return 404 because the deleted data is re-queried.   
To prevent that, we can tell to invalidate the cache, but also, do not fetch it again for any opened component. For that, we add the **refetchType:’none’** property, to the **queryClient.invalidateQueries** object argument.

### Optimistic Updating

When we update a record on a page, we could use the updated value in the FE while the BE is being updated. This is called optimistic updating which optimistically already installed the updated value in the FE while the BE did not acknowledge yet, that the change is effective.

To do that, useMutation accept three other functions:

- **onMutate**. It is a function executed after the mutate function. There, we get the data that was passed to mutate. We must cancel any request with the same key; get the previous data and install the data which was passed to the mutate function (that is the optimistic update logic). Note that the queryKey are the useQuery queryKey. The previous value should be returned in an object so we can set back the previous value.  
- **onError**. This function is executed after the request returns. There, we can install the previous data by using the context argument.  
- **onSettle**. this function is always executed. There we can invalidate any query, so that any difference with the BE is refreshed. This will thus restart a query for any visible component using this key for a query.

| import { Link, useNavigate, useParams } from "react-router-dom"; ... export default function EditEvent() {   const navigate \= useNavigate();   const { id } \= useParams();   const { data, isLoading, isError, error } \= useQuery({     queryKey: \["events", id\],     queryFn: (obj) \=\> fetchEvent(obj, id),   });   const { mutate } \= useMutation({     mutationFn: updateEvent,     onMutate: async (data) \=\> {       await queryClient.cancelQueries({ queryKey: \["events", id\] });       const previousEvent \= queryClient.getQueryData(\["events", id\]);       queryClient.setQueryData(\["events", id\], data.updatedEvent.event);       return { previousEvent };     },     onError: (error, data, context) \=\> {       queryClient.setQueryData(\["events", id\], context.previousEvent);     },     onSettled: () \=\> {       queryClient.invalidateQueries(\["events", id\]);     },   });   function handleSubmit(formData) {     mutate({ id, updatedEvent: { event: formData } });     navigate("../");   }      ... } |
| :---- |

### 

[image1]: React_images/image1.png

[image2]: React_images/image2.png

[image3]: React_images/image3.png

[image4]: React_images/image4.png

[image5]: React_images/image5.png

[image6]: React_images/image6.png

[image7]: React_images/image7.png

[image8]: React_images/image8.png

[image9]: React_images/image9.png

[image10]: React_images/image10.png

[image11]: React_images/image11.png

[image12]: React_images/image12.png

[image13]: React_images/image13.png

[image14]: React_images/image14.png

[image15]: React_images/image15.png

[image16]: React_images/image16.png

[image17]: React_images/image17.png

[image18]: React_images/image18.png
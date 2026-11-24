from  
[https\://learning.oreilly.com/course/understanding-typescript/9781789951905/](https://learning.oreilly.com/course/understanding-typescript/9781789951905/)

# Getting Started

Typescript is Javascript with syntax for types.  
Typescript is not run in the browser; it needs to be transpiled.  
[Node.Js](http://Node.Js) must be installed (use msi file found on [https\://nodejs.org/en/download](https://nodejs.org/en/download)). Then use the command “npm install \-g typescript”, which will install typescript compiler globally on the machine. You can use “tsc \-v” to ensure that it is installed. This will print the version of the compiler.  
To compile a file “basic.ts”

```
tsc basic.ts
```

To execute the js code

```
node basic.js
```

# TypeScript Basics & Basic Types

## Working with Types & Exploring Built-in Types

We can assign a type to a variable at declaration:

```ts
let userName: string = "gatien";
let userName2 = "gatien";
```

## Type Inference vs Type Assignment

Like in C++ and C\# there is a type inference which prevents us from writing the type at assignment. The two following line are the same.

```ts
let userName: string = "gatien";
let userName2 = "gatien";
```

## Assigning Types to Functions

function can have typed parameters and return. Type inference works on optional parameters. A function has a type too.

```ts
type AddFunctionType = (a: number, b?: number) => number;

const add: AddFunctionType = function (a: number, b = 10): number {
  return a + b;
};
```

## The "any" Type

The any type exist and allow to store any type in a variable but it should be not used:

```ts
let userAge: any = 23;
userAge = true;
```

## Understanding Union Types

Union types are used to tell that a variable can contain one of the types separated with a pipe:

```ts
let userAge: number | boolean = 23;
userAge = true;
```

## Arrays & Types

```ts
// array of string
let values1: string[] = [];
values1.push("true");

// array of union
let values2: (number | boolean)[] = [];
values2.push(true);

// generic array of union
let values3: Array<number | boolean> = [];
values3.push(true);
```

Here Array\<T\> is a generic type.

## Tuples

```ts
// tuple of a string and number
let tuple: [string, number] = ["gatien", 38];
tuple[0]; // reading
tuple[0] = "mathilde"; //writing
console.log(tuple);
```

## Object types

```ts
// declare the type
type user = { age: number; name: string };
let user1: user = { name: "gatien", age: 38 };

// similar to
let user2: { age: number; name: string } = { name: "gatien", age: 38 };
```

## The "Must Not Be Null" Type

There is a variant of any type which cannot be assigned to null or undefined:

```ts
// declare the type
let obj: {};
obj = { name: "gatien" };
obj = null; // not allowed
obj = undefined; // not allowed
```

## Flexible Objects with the Record Type

The Record\<K,V\> type is the C++ std::map:

```ts
type User = { name: string; age: number };

let rec: Record<number, User> = {
  1: { name: "gatien", age: 38 },
};
console.log(rec[1].name); //print gatien

rec[3] = { name: "mathilde", age: 35 };
console.log(rec[3].name); //print mathilde
```

## Working with Enums

The enum in ts are stored as integers by default, but we can have a string instead.

```ts
enum Role {
  Admin = "Admin",
  EndUser = "EndUser",
  KeyUser = "KeyUser",
}

enum action {
  Read,
  Writte,
}

const printEnum = function (r: {}): void {
  console.log(r.toString());
};

printEnum(Role.Admin); //print Admin
printEnum(action.Read); //print 0
```

## Being Specific with Literal Types

Literal types are alternative to enum types:

```ts
type Role = "Admin" | "EndUser" | "KeyUser";
let role: Role = "KeyUser";

const printEnum = function (r: {}): void {
  console.log(r.toString());
};

printEnum(role); //print KeyUser
```

## The "never" Type

The never type indicates that function will throw an exception:

```ts
type Logger = (message: string) => never;

const add: Logger = function (a: string): never {
  console.log(a);
  throw new Error(a);
};
```

## null & undefined \- Special Types

We can tell that a variable contains only null or undefined by specifying its type as null or undefined. This is not very useful but in combination with another type, in a union, it means the variable is either a type or null/undefined:

```ts
let a: string | null | undefined;
a = undefined;
a = null;
a = "hello";
```

## Forced "Not Null"

We can narrow the type of a variable with the exclamation mark to indicate that the value on the left is not null. This mutes TS and lets it thrust the developer. If the hypothesis is not true, there is a runtime error and because the compilation error is muted.

```ts
type User = { name: string };
type UserLikely = User | null;

const LogUser = function (user: UserLikely): void {
  console.log(user!.name);
};

LogUser({ name: "gatien" });
LogUser(null); // runtime error
```

## Type casting

when we know that a type is another one (because it inherits from the other), we can perform type casting with the **as** operator. This also convinces TS that the code is correct.

```ts
type User = { name: string };
let obj: object = { name: "gatien" };
const castedObj = obj as User;
console.log(castedObj.name);

type Role = { role: () => void };
let badlyCasted = obj as Role;
console.log(badlyCasted.role()); //runtime error
```

The runtime error does not occur at casting.

## The "unknown" Type

unknown is a type which tells that the variable type is unknown (like any) but it forces the developers to write if-clauses to be sure of the type of a variable, with the use of **typeof** and with the **in** operator to check if a property is in the unknown variable.

## Optional Values

Optional type means that it may be undefined. We mark it with a question mark after the variable name.

```ts
function log(message?: string): void {
  console.log(message ?? "default message");
}

type User = { name: string; age: number; role?: string };
let u: User = { name: "Gatien", age: 38 };

log(); // print default message
console.log(u.role); // print undefined
log("hello"); // print hello
```

**It is a difference with C\# and C++ where this can only be made with default argument value.**

## Rest Parameters

like in JS, it is possible to accept any number of arguments of the same type with the triple dot operator:

```ts
const add = function (...args: number[]): number {
  let total = 0;
  for (const elt of args) {
    total += elt;
  }
  return total;
};

console.log(add(1, 2, 3, 4));
```

it is also possible to store the values in tuples, but then is a fixed number of values:

```ts
const add = function (...args: [number, number]): number {
  let total = 0;
  for (const elt of args) {
    total += elt;
  }
  return total;
};

console.log(add(1, 2));
```

## Readonly properties

We can make sure a property value can never be overwritten with the **readonly** keyword.

```ts
type User = {
  readonly name: string;
  age: number;
};

const gatien: User = {
  name: "gatien",
  age: 38,
};

gatien.age = 39;
gatien.name = "mathilde"; // compiler error
```

# The TypeScript Compiler

First we need to create the compiler config file with:

```
tsc --init
```

Documentation of this tsconfig.json file is at [https\://aka.ms/tsconfig](https://aka.ms/tsconfig).

In this file, there are two important settings that tell where to find the code to compile and where to compile the js code. The following means that the directory src contains the TS code and dist will contain the JS compiled code. Those directory should be in the same directory as the tsconfig.json file.

```json
{
  ...
  "rootDir": "./src",
  "outDir": "./dist",
  ...
}
```

Another interesting option is the target. It tells to which version of JS we want to compile the TS code. Using esnext, would indicate to typescript to compile to a version of JS which includes every future feature (including decorator). As node might not know the latest JS feature (like decorator), converting to es2022 is rather a safe approach.

```json
{
  ...
  "target": "es2022",
  ...
}
```

to compile the code, simply use the following command:

```
tsc
```

or to let the compiler recompile every time a change is made:

```
tsc --watch
```

# Classes and Interfaces

## Classes

Class definitions are very similar to vanilla JS. There is a constructor, we use the class keyword, we must declare every member in the classes and they are public by default.

```ts
class User {
  constructor(name: string) {
    this.name = name;
  }

  name: string;
  private isAlive = true; // default initialization
}

const user = new User("Gatien");
console.log(user.name);
```

Like in C++ and C\#, there is a quick way to initialize properties. We must use the word public or private in front:

```ts
class User {
  constructor(private readonly name: string, public age: number) {}

  greet() {
    console.log(`I'm ${this.name}`);
  }
}

const user = new User("Gatien", 38);
console.log(user.age);
user.greet();
```

**readonly** properties means that the property cannot be reassigned. It is like const is JS. It is the same concept as in C\#.

the get keyword can be added next to a method name to tell that a property or calculated property can be retrieved:

```ts
class User {
  constructor(
    private readonly firstName: string,
    private readonly lastName: string
  ) {}

  get fullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
}

const user = new User("Gatien", "De Bast");
console.log(user.fullName);
```

Same for setters:

```ts
class User {
  private _job?: string;

  constructor(private readonly _name: string) {}

  set job(job: string) {
    this._job = job;
  }
}

const user = new User("Gatien");
user.job = "Developer";
```

Static methods and properties are similar to C++ and C\#:

```ts
class User {
  private static _type: string = "User";

  constructor(private readonly _name: string) {}

  static greet(): void {
    console.log(`I'm ${User._type}`);
  }

  greet(): void {
    console.log(`I'm ${this._name}, that's my name as ${User._type}`);
  }
}

const user = new User("Gatien");
user.greet();
User.greet();
```

## Inheritance

We can inherit from another class with the **extends** keyword. protected members can be accessed by derived classes. **Compared with C++, we cannot redefine the accessibility level of a property to be less public. Compared with C++, it is allowed to override members.**

```ts
class User {
  constructor(protected readonly _name: string) {}

  greet() {
    console.log(`I'm ${this._name}`);
  }
}

class Employee extends User {
  constructor(private _jobTitle: string, protected readonly _name: string) {
    super(_name);
  }

  greet() {
    console.log(`I'm ${this._name}, I'm a ${this._jobTitle}`);
  }
}

const user = new User("Gatien");
const employee = new Employee("Developer", "Gatien");
user.greet();
employee.greet();
```

An abstract class is meant to always be derived from and not instantiated:

```ts
abstract class User {
  constructor(protected readonly _name: string) {}
}

class Employee extends User {
  constructor(private _jobTitle: string, protected readonly _name: string) {
    super(_name);
  }

  greet() {
    console.log(`I'm ${this._name}, I'm a ${this._jobTitle}`);
  }
}

const employee = new Employee("Developer", "Gatien");
employee.greet();
```

## Interfaces

interfaces are defined with the interface keywords. They must be implemented by another class or by a JS object:

```ts
interface IUser {
  greet(): void;
}

class Employee implements IUser {
  constructor(
    private readonly _jobTitle: string,
    private readonly _name: string
  ) {}

  greet(): void {
    console.log(`I'm ${this._name}, I'm a ${this._jobTitle}`);
  }
}

const user: IUser = {
  greet() {
    console.log(`I'm a simple user`);
  },
};

const employee = new Employee("Developer", "Gatien");
employee.greet();
user.greet();
```

We can declare multiple time the same interface so that all definitions are merged in one:

```ts
interface IUser {
  name: string;
}

interface IUser {
  greet(): void;
}

class Employee implements IUser {
  constructor(private readonly _jobTitle: string, public name: string) {}

  greet(): void {
    console.log(`I'm ${this.name}, I'm a ${this._jobTitle}`);
  }
}

const employee: IUser = new Employee("Developer", "Gatien");
employee.name = "Mathilde";
employee.greet();
```

Multiple interface implementation is possible:

```ts
interface IUserWithName {
  name: string;
}

interface IUserWithGreet {
  greet(): void;
}

class Employee implements IUserWithGreet, IUserWithName {
  constructor(private readonly _jobTitle: string, public name: string) {}

  greet(): void {
    console.log(`I'm ${this.name}, I'm a ${this._jobTitle}`);
  }
}

const employee: IUserWithGreet = new Employee("Developer", "Gatien");
employee.greet();
```

It is also possible to extend interfaces:

```ts
interface IUserWithName {
  name: string;
}

interface IUser extends IUserWithName {
  greet(): void;
}

class Employee implements IUser {
  constructor(private readonly _jobTitle: string, public name: string) {}

  greet(): void {
    console.log(`I'm ${this.name}, I'm a ${this._jobTitle}`);
  }
}

const employee: IUser = new Employee("Developer", "Gatien");
employee.greet();
```

# Advanced Types

## Intersection type with &

Intersection types are types that combine multiple types. The goal is to have reusable pieces of data. Types are combined with **&**. It is a kind of inheritance.

```ts
type FileData = { path: string; content: string };
type DatabaseDate = { url: string };
type Status = { isOpen: boolean; errorMessage?: string };

type AccessedFileDate = FileData & Status;
type AccessedDatabaseData = DatabaseDate & Status;

const file: AccessedFileDate = {
  path: "path",
  content: "content",
  isOpen: true,
};

const data: AccessedDatabaseData = {
  url: "url",
  isOpen: true,
};
```

## Type guard

This is a technique to ensure that only one type is possible in a scope, when giving a union type or unknown type. Typescript compiler will be sure that the type is known, when in this scope.

### in operator

The first technique is to use the **in** operator to check if a discriminating property is in the union.

```ts
type FileSource = { path: string };
const fileSource: FileSource = {
  path: "some/path/to/file.csv",
};

type DBSource = { connectionUrl: string };
const dbSource: DBSource = {
  connectionUrl: "some-connection-url",
};

type Source = FileSource | DBSource;

function loadData(source: Source) {
  console.log(source.path); // compiler error
  if ("path" in source) {
    console.log(source.path);
    return;
  }
  console.log(source.connectionUrl);
}
```

### discriminating union

The second technique is to add a shared property like **type**, to the unions, and discriminating on them

```ts
type FileSource = { type: "file"; path: string };
const fileSource: FileSource = {
  type: "file",
  path: "some/path/to/file.csv",
};

type DBSource = { type: "db"; connectionUrl: string };
const dbSource: DBSource = {
  type: "db",
  connectionUrl: "some-connection-url",
};

type Source = FileSource | DBSource;

function loadData(source: Source) {
  if (source.type === "file") {
    console.log(source.path);
    return;
  }
  console.log(source.connectionUrl);
}
```

### class and instanceof

Another way to discriminate is when the object is an instance of a class so we can use **instanceof**.

```ts
class User {
  constructor(public name: string) {}

  join() {
    console.log(`${this.name} is joining.`);
  }
}

class Admin {
  constructor(permissions: string[]) {}

  scan() {
    console.log("scanning");
  }
}

const user = new User("Max");
const admin = new Admin(["ban", "restore"]);

type Entity = User | Admin;

function init(entity: Entity) {
  if (entity instanceof User) {
    entity.join();
    return;
  }
  entity.scan();
}

init(user);
```

### Type predicate

In modern typescript we can outsource the check to another function which returns a type with **is**. This is called a type predicate.

```ts
type FileSource = { type: "file"; path: string };
const fileSource: FileSource = {
  type: "file",
  path: "some/path/to/file.csv",
};

type DBSource = { type: "db"; connectionUrl: string };
const dbSource: DBSource = {
  type: "db",
  connectionUrl: "some-connection-url",
};

type Source = FileSource | DBSource;
const s: Source = fileSource;

function isFile(source: Source): source is FileSource {
  return source.type == "file";
}

if (isFile(s)) {
  console.log(s.path);
}
```

### Function overload

If we pass a union to a function, and this function returns either one type or another, the returned type is a union. Nothing new compared to what we know about unions.

```ts
function desc(val: string | any[]) {
  if (typeof val === "string") {
    const numberOfWords = val.split(" ").length;
    return `${numberOfWords} words`;
  }
  return val.length;
}

const desc1: string | number = desc("Hello world");
const desc2: string | number = desc(["mathilde", "camille"]);
```

However, if we use function overloading, by mapping the input to the output type, typescript infer the type.

```ts
function desc(val: string): string;
function desc(val: any[]): number;
function desc(val: string | any[]) {
  if (typeof val === "string") {
    const numberOfWords = val.split(" ").length;
    return `${numberOfWords} words`;
  }
  return val.length;
}

const desc1: string = desc("Hello world");
const desc2: number = desc(["mathilde", "camille"]);
```

## Index Types

In typescript we can tell that an object has any number of property names (like a std::map has many key-value pairs). This is defined by using the square bracket as placeholder property. The type of the property names must be given (like in a map). The value type must be defined too.  
Only string, number and Symbol are allowed as property types.

```ts
type Storage = { [prop: string]: string | number };

let store: Storage = {};
store.id = "local storage";
store.capacity = 10;
```

This is very similar as Record type.

## Constant type with “as const”

**as const** indicates that the type of the variable can only be the defined value. Therefore it is like a constant which cannot be changed. For instance, if we define an array of roles as constant, it means this array cannot be changed, and if we take the first value, we know it is a literal.

```ts
type Roles = readonly ["admin", "guest", "editor"];
let roles: Roles = ["admin", "guest", "editor"] as const;

type Admin = "admin";
const admin: Admin = roles[0];
```

## the satisfies keyword

**satisfies** is used at variable assignment without assigning a precise type. It lets the type inference work, but enforce that this type is satisfying some constraint, like being a Record of string-\>object.  
satisfies asks typescript to check that the assignment satisfies a type but lets the type inference assign a stricter type.

```ts
type Endpoint = {
  method: "GET" | "POST" | "DELETE";
  path: string;
};

const endpoints = {
  places: { method: "GET", path: "/Places" },
  deletePlace: { method: "DELETE", path: "/Places" },
} satisfies Record<string, Endpoint>;
```

The above makes sure that any added endpoint follows a certain pattern, but the type of the endpoints variable is accurate (it has two properties). Developers are enforced to respect the pattern.

```ts
type Endpoint = {
  method: "GET" | "POST" | "DELETE";
  path: string;
};

const endpoints = {
  places: { method: "GET", path: "/Places" },
  deletePlace: { method: "DELETE", path: "/Places" },
  updatePlaces: { method: "PUT", path: "/Places" }, // compilation error
} satisfies Record<string, Endpoint>;
```

# Generic Types

## Creating and using generic type

generic types are like template in C++ or generic types in C\#. We can create them as normal struct object.

```ts
type DataStore<T> = { value: T };
type BooleanDataStore = DataStore<boolean>;
type StringDataStore = DataStore<string>;

const boolStore: BooleanDataStore = { value: true };
const boolStore2: DataStore<boolean> = { value: false };

type KeyValuePair<K, V> = { key: K; value: V };

// compiler error : parameter type cannot be a generic type
type KeyValueDataStore<K, V> = { [property: K]: V };
```

## Generic function and inference

```ts
function merge<T>(a: T, b: T) {
  return [a, b];
}

const merged = merge("Mathilde", "Gatien"); // merged is string[]
const mergedBool = merge<boolean>(true, ""); // compiler error
```

## extends keyword

This keyword in the definition of the generic (a function, a class or an object) forces developers to give a template argument that extends a type.

```ts
function mergeObj<K, T extends Record<string, K>>(a: T, b: T) {
  return { ...a, ...b };
}

const newObj = mergeObj({ name: "Gatien" }, { firstName: "De Bast" });
console.log(newObj);
```

## Generic class

```ts
class User<T> {
  constructor(private m_id: T) {}

  get id(): T {
    return this.m_id;
  }
}

let gatien = new User<string>("Gatien");
let jew = new User<number>(1);
console.log(gatien.id); // print : Gatien
console.log(jew.id); // print : 1
```

## Full Example

```ts
class LinkedListNode<V> {
  constructor(
    public value: V,
    public previous: LinkedListNode<V> | null,
    public next: LinkedListNode<V> | null
  ) {}
}

type NodeVisitor<V> = (value: V) => void;

class LinkedList<V> {
  constructor() {}

  public addFront(value: V): void {
    const oldFrontNode = this.m_frontNode;
    const newElement = new LinkedListNode<V>(value, null, oldFrontNode);
    if (oldFrontNode !== null) oldFrontNode.previous = newElement;
    this.m_frontNode = newElement;
  }

  public visit(visitor: NodeVisitor<V>): void {
    let currentNode = this.m_frontNode;
    while (currentNode !== null) {
      visitor(currentNode.value);
      currentNode = currentNode.next;
    }
  }

  private m_frontNode: LinkedListNode<V> | null = null;
}

function logValue(value: string) {
  console.log(value);
}

const list = new LinkedList<string>();
list.addFront("Albert");
list.addFront("Gatien");
list.addFront("Mathilde");
list.addFront("Aubert");
list.visit(logValue);
```

# Deriving Types from Types

## Types from variables with typeof

typeof usually returns a string being the type of the variable in JS. In TS, With **typeof**, we can derive type of a variable when creating a type. Mind that const on primitive types (string and number) will make sure that only the value can be put it the derived type.

```ts
type User = { name: string; age: number };

const role = "Admin";
const exp = 1000;
const gatien: User = { name: "gatien", age: 38 };

type UserRole = { user: typeof gatien; role: typeof role; exp: typeof exp };

const gr: UserRole = {
  // "user" can contain any name and age
  user: { name: "mathilde", age: 34 },
  // "role" and "exp" can only be "Admin"
  // and 1000 because the variable is a primitive const
  role: "Admin",
  exp: 1000,
};
```

## Types from Type properties with keyof

keyof is a TS-only keyword. In combination with a type, it creates a union type of all key names as string.

```ts
type User = { name: string; age: number };
type UserKeys = keyof User; // union type

const key1: UserKeys = "name";
const key2: UserKeys = "age";
const key3: UserKeys = "address"; // compiler error
```

We can also use keyof to constrain the type of a generic argument, if one of the function parameter should be one of the key of one of the other parameter:

```ts
function getProp<V extends object, K extends keyof V>(obj: V, key: K) {
  return obj[key];
}

const gatien = { name: "gatien", age: 38 };
console.log(getProp(gatien, "age")); // 38
```

## Deriving sub types

We can define a sub-type from a type with accessing the property name. If we have an array of object, we can also access the type of the objects in this array.

```ts
type AppUser = {
  name: string;
  age: number;
  permissions: [{ id: string; title: string; desc: string }];
};

type Perms = AppUser["permissions"]; // array of permissions
type Perm = AppUser["permissions"][number]; // a single permission type
```

## Mapped types: deriving properties for type properties

Mapped types can be made with union types, with the in operator. They constrain each property to be a value of the union. In the following example, we declare PermissionHandler a type which property names are mapped to a Union type value,

```ts
type ReadPermissions = "no-read" | "read";

type PermissionHandlers = {
  [permission in ReadPermissions]: () => void;
};
```

Mapped types have the same properties of another type. It can be useful if we want to base one type on the properties of another.

```ts
type Operations = {
  add: (a: number, b: number) => number;
  substract: (a: number, b: number) => number;
};

type Result = {
  [resultof in keyof Operations]: number;
};

const operations: Operations = {
  add: (a, b) => a + b,
  substract: (a, b) => a - b,
};

const result: Result = {
  add: operations.add(1, 1),
  substract: operations.substract(1, 1),
};
```

They can be generic types:

```ts
type Operations = {
  add: (a: number, b: number) => number;
  substract: (a: number, b: number) => number;
};

type Result<O> = {
  [resultof in keyof O]: number;
};
```

A mapped type properties include the optional (?) and readonly constraints.

```ts
type Operations = {
  readonly add: (a: number, b: number) => number;
  substract?: (a: number, b: number) => number;
};

type Result = {
  // add is readonly and substract is optional
  [resultof in keyof Operations]: number;
};
```

If the based type has optional properties, we can remove this constraint with **\-?**. it means that the derived type should have the properties while the based type does not. Same for readonly, with **\-readonly** in front.

```ts
type Operations = {
  add?: (a: number, b: number) => number;
  readonly substract: (a: number, b: number) => number;
};

type Result = {
  -readonly [resultof in keyof Operations]-?: number;
};

const operations: Operations = {
  add: (a, b) => a + b,
  substract: (a, b) => a - b,
};

const result: Result = {
  add: operations.add(1, 1),
  substract:
    operations.substract !== undefined ? operations.substract(1, 1) : 1,
};
```

## Template literal types

We can derive a new union type, with the combinations of union types, with template literals:

```ts
type ReadPermissions = "no-read" | "read";
type WritePermissions = "no-write" | "write";

// contains all combinations:
// - "no-read-write"
// - "no-read-no-write"
// - "read-write"
// - "read-no-write"
type FilePermission = `${ReadPermissions}-${WritePermissions}`;
```

We can derive union types with template literal and keyof. In combination with mapped type feature, it is possible to make types with properties equivalent to another source type.

```ts
type Rivers = {
  danube: string;
  meuse: string;
  rhin: string;
};

// "SourceOf-danube" | "SourceOf-meuse" | "SourceOf-rhin"
type RiversProperty = `SourceOf-${keyof Rivers}`;

type RiverSources = {
  [source in RiversProperty]: string;
};
```

## Conditional types

This TS features allows to derive types from types conditionally. We use a ternary operator to make the condition.

```ts
type StringArray = string[];
type Element<A> = A extends any[] ? A[number] : A;

// string
type StringElt = Element<StringArray>;
// number
type Number = Element<number>;
```

with the **infer** keyword, we can extract the type nested in the checked type. For instance, we can extract the element type in an array, the returned and output type of a function, and the argument type of a generic type.

```ts
// infer that string is the element type
type StringArray = string[];
type Element<A> = A extends (infer E)[] ? E : never;
type String = Element<StringArray>;

// infer that number is the input type and boolean is the output type
type Function = (a: number) => boolean;
type Arg<F> = F extends (a: infer R) => any ? R : never;
type Out<F> = F extends (a: any) => infer O ? O : never;
type Boolean = Out<Function>;
type Number = Arg<Function>;

// infer the generic type
type PromisedValue<P> = P extends Promise<infer V> ? V : never;
type PromisedString = PromisedValue<Promise<string>>;
```

## Typescript utility types

Some use-cases of deriving types from types, are already covered in typescript utility types:  
[https\://www\.typescriptlang.org/docs/handbook/utility-types.html](https://www.typescriptlang.org/docs/handbook/utility-types.html)

# JS Decorator

Decorator is code changing the behavior of the main code. The decorators are standard JS functionality while experimental decorators are TS functionality. Experimental decorators are old decorator because they were made by TS before JS supported it.

A decorator is an OOP feature, so we can only build decorator for classes, methods, fields, getter and setters.

## Class decorator

A class decorator is a generic function with two arguments:

- a target, this is the class itself.
- a context, of type ClassDecoratorContext

This decorator is written at the top of the class and executed when the class is discovered. It can modify the class by extending the class with new members. The generic argument is **new (...args: any\[\]** which means that it is a class.

In the following example we add the age property, but it is not accessible by the caller of Person.

```ts
const age = function <T extends new (...args: any[]) => any>(
  target: T,
  ctx: ClassDecoratorContext
) {
  return class extends target {
    age = 35;
  };
};

@age
class Person {
  name = "Max";
}

const p = new Person();
console.log(p);
console.log(p.age); // compiler error
```

In this example, we change the constructor to add a logging phase, at construction:

```ts
const logger = function <T extends new (...args: any[]) => any>(
  target: T,
  ctx: ClassDecoratorContext
) {
  return class extends target {
    constructor(...args: any[]) {
      super(...args);
      console.log("class constructor");
      console.log(this);
    }
  };
};

@logger
class Person {
  name = "Max";
}

const p = new Person();
```

## Method decorator

The auto-bind use case

In method decorator function, the context contains some information like its static and private characteristics and its name. it also contains the **addInitializer** method which gives access to the constructor of the class of the method which we are attaching a decorator to.

In JS, the this keyword in a method, is the instance that executes the method. If we take a pointer to this method, the this keyword is lost. This can be observed, because while two pointers to an instance are not the same, the pointer to their method is the same, indicating that the method lost the instance.

```ts
class Person {
  name = "Max";

  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}

const p = new Person();
const j = new Person();
const pGreet = p.greet;
const jGreet = j.greet;

console.log(p === j); // print false as not the same memory
console.log(pGreet === jGreet); // print true as same memory
jGreet(); // runtime error because this is lost
```

To solve this issue, JS has the bind method which binds an object to a method, so we can use it in the future:

```ts
class Person {
  name = "Max";

  constructor() {
    this.greet = this.greet.bind(this);
  }

  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}

const p = new Person();
const j = new Person();
const pGreet = p.greet;
const jGreet = j.greet;

console.log(p === j); // print false as not the same memory
console.log(pGreet === jGreet); // print false as different binded object
jGreet(); // works
```

A common use case of the decorator for method is the autobind which automatically binds the instance of the class to the method:

```ts
const autobind = function (target: Function, ctx: ClassMethodDecoratorContext) {
  ctx.addInitializer(function (this: any) {
    this[ctx.name] = this[ctx.name].bind(this);
  });
};

class Person {
  name = "Max";

  @autobind
  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}

const p = new Person();
const j = new Person();
const pGreet = p.greet;
const jGreet = j.greet;

console.log(p === j); // print false as not the same memory
console.log(pGreet === jGreet); // print true as same memory
jGreet(); // runtime error because this is lost
```

replacing the method execution

Replacing the body of the method is done with the following. Observe the **this** and **args** argument passed to the original method with **target.apply**. The args can be typed if we expect a certain type as argument.

```ts
const log = function (target: Function, ctx: ClassMethodDecoratorContext) {
  return function (this: any, ...args: any[]) {
    console.log(`executing ${ctx.name.toString()}`);
    target.apply(this, args);
  };
};

class Person {
  name = "Max";

  @log
  greetWithPrefix(message: string) {
    console.log(`${message}, I'm ${this.name}`);
  }

  @log
  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}

const p = new Person();
p.greetWithPrefix("hello again");
p.greet();
```

## Field operator

A field decorator is also a function with an undefined target.  
we can change the initial value of the field by returning a function.

```ts
const fieldLog = function (target: undefined, ctx: ClassFieldDecoratorContext) {
  return (initialValue: string) => {
    console.log("decorator");
    return initialValue + " De bast";
  };
};

class Person {
  @fieldLog
  name = "Gatien";

  constructor() {
    console.log("constructor");
  }

  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}

const p = new Person();
p.greet(); // Gatien De Bast
```

## Decorator Factory

A decorator factory is a function returning a decorator, therefore if we execute it inside the class, we get a decorator which will do its job:

```ts
function replacer(suffix: string) {
  return function (target: undefined, ctx: ClassFieldDecoratorContext) {
    return (initialValue: string) => {
      return initialValue + suffix;
    };
  };
}

class Person {
  @replacer("De Bast")
  name = "Gatien";

  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}

const p = new Person();
p.greet(); // Gatien De Bast
```

# TS Experimental Decorator

The experimental decorator is the old TS support for decorators. You’ll need to enable them in tsconfig.json with:

```json
{
  "experimentalDecorators": true
}
```

# Namespaces and Modules

Namespace and modules are two concepts used to separate code in different file bundles.

## Namespaces

This is the old way. We usually separate two files like the following. Any entity that wants to use the namespace, should be in the same namespace.

```ts
namespace GDB {
  export class Person {
    name: string = "";
    constructor(name: string) {
      this.name = name;
    }
  }
}
```

```ts
/// <reference path="gdb-person.ts" />
namespace GDB {
  const p = new Person("Gatien");
}
```

A problem with namespace is similar to the transitive include of C++: if one of the referred file, referred to another file used by the first one, it works. For instance if a first file c.ts uses class A, defined in file [a.ts](http://a.ts), it can get it transitively if file [c.ts](http://c.ts) imports file [b.ts](http://b.ts), which imports [a.ts](http://a.ts). If the transitive file (b.ts), remove its import (of a.ts), the compiler does say anything but the app won’t work.

Moreover, the “import” syntax of the namespace does not say what is imported.

## Modules

The ES/JS module feature needs to be activated in the package.json via:

```json
{
  "type": "module"
}
```

The separation in multiple files make use of the standard ES/JS keywords **import** and **export**. After the **from** keyword, a relative path is expected. Mind the **.js** if the module in tsconfig.json is "nodenext."

```ts
export class Person {
  name: string = "";
  constructor(name: string) {
    this.name = name;
  }
}
```

```ts
import { Person } from "./gdb-person.js";

const p = new Person("Gatien");
console.log(p);
```

If there are multiple export, rather then import them all inside the {}, we can use the **\* as** notation. After as, we given alias which will bundle all export in an object:

```ts
export class Person {
  name: string = "";
  constructor(name: string) {
    this.name = name;
  }
}

export const author = new Person("THE ONE");
```

```ts
import * as People from "./gdb-person.js";

const p = new People.Person("Gatien");
console.log(p);
console.log(People.author);
```

The as keyword also works inside {} for each imported entity, to give them an alias.

If a file contains only one export, we may use the **default** keyword. In the import, the imported entities can get an alias without the as keyword. This is why the default export, can be an anti-pattern (renaming an entity does not trigger a compilation error).

```ts
export default class Person {
  name: string = "";
  constructor(name: string) {
    this.name = name;
  }
}
```

```ts
import Person from "./gdb-person.js";

const p = new Person("Gatien");
console.log(p);
```

if an **ES module is imported twice in different files**, it is not executed multiple times. **It is executed once**.

# Typescript projects with Vite

Starting from (containing a basic html, css and ts files): https\://github.com/mschwarzmueller/understanding-typescript-resources/blob/main/attachments/15-build-tools-vite/starting-project.zip

If we only use the ts compiler, we just transform the ts code into js code.  
We need a bundler to group all files together. Vite is a bundler.

The Vite documentation ([https\://vite.dev/guide/](https://vite.dev/guide/)) indicates how to create a new project from scratch with the following command. This should be executed at the start of the project.

```
npm create vite@latest
```

This will install a preset demo project which you can run with “npm run dev”.

# Webpack and Typescript

Webpack is a bundler too. It is a tool that helps bundling js code together to limit the http request to the server to get the JS. Usually there is a http request per import. Moreover, the code is not small and optimized for network discussion between the client and the server of js, html and css files. Webpack also optimizes our code. It minifies the code.

# Third party libraries

## Using JS libraries

There are some libraries in JS which we want to use in TS project. For instance, lo-dash or node library can be installed with:

```
npm install --save lodash
npm install --save node
```

However, this is not the package to install in TS, it is:

```
npm install --save-dev @types/lodash
npm install --save-dev @types/node
```

Now we can use lo-dash and the type-script code can be found in the “node_module/@type/lodash” directory. the [d.ts](http://d.ts) files, contain the type definition so typescript understand.

```ts
import _ from "lodash";

let numbers: number[] = [1, 2, 3, 4, 5];
let result = _.chunk(numbers, 2);
console.log(result);
```

## Using TS libraries

Zod

To install Zod for instance:

```
npm install zod
```

Zod is a run-time type check. For instance, we can check that a payload (a json in “data.json” for instance) has the right format. In particular, the z.infer generic allow us to access the type of the schema so it can be used in functions:

```json
{
  "title": "test",
  "id": 5,
  "values": ["1", "3"]
}
```

```ts
import z from "zod";
import fs from "node:fs";

const dataSchema = z.object({
  title: z.string(),
  id: z.number(),
  values: z.array(z.string()),
});

type Data = z.infer<typeof dataSchema>;

function logData(data: Data) {
  console.log(data);
}

const content: any = JSON.parse(fs.readFileSync("data.json").toString());
const parsedData: Data = dataSchema.parse(content);
logData(parsedData);
```

Axios

Another library is Axios, which gives the possibility to use http request:

```
npm install axios
```

```ts
import axios from "axios";

type StartWarPeople = {
  name: string;
};

axios.get<StartWarPeople>("https://swapi.dev/api/people/1").then((response) => {
  console.log(response.data.name); // prints Luke Skywalker
});
```

# React and Typescript

## Starting a project with Vite

From a blank folder execute, where react-ts is the project name.

```
npm create vite@latest react-ts
```

From that, choose React, Typescript and a linter (ESLinter). After, we can run the project with:

```
npm run dev
```

## Component props

We can type the props of a React component:

```tsx
type HeaderProps = {
  image: {
    src: string;
    alt: string;
  };
};

export default function Header({ image }: HeaderProps) {
  return (
    <header>
      <img {...image} />
    </header>
  );
}
```

Then using the component would be done with the following code. In this code, the goalImg variable will contain the path to the image.

```tsx
import Header from "./components/Header";
import goalImg from "./assets/goals.jpg";

export default function App() {
  return (
    <main>
      <Header image={{ src: goalImg, alt: "list of goals" }} />
    </main>
  );
}
```

## Children props

With a children prop, the type is **ReactNode**

```tsx
import { type ReactNode } from "react";

type HeaderProps = {
  image: {
    src: string;
    alt: string;
  };
  children: ReactNode;
};

export default function Header({ image, children }: HeaderProps) {
  return (
    <header>
      <img {...image} />
      {children}
    </header>
  );
}
```

Which is used like:

```tsx
import Header from "./components/Header";
import goalImg from "./assets/goals.jpg";

export default function App() {
  return (
    <main>
      <Header image={{ src: goalImg, alt: "list of goals" }}>
        <h1>Your Course Goals</h1>
      </Header>
    </main>
  );
}
```

## Component as Functional Component (FC)

An alternative way of defining a React TS component is with using the generic FC type:

```tsx
import type { FC } from "react";

type Goal = {
  id: number;
  title: string;
  description: string;
};

type CourseGoalsProps = {
  goals: Goal[];
};

const CourseGoals: FC<CourseGoalsProps> = ({ goals }: CourseGoalsProps) => {
  return (
    <ul>
      {goals.map((goal) => (
        <li key={goal.id}>
          <article>
            <div>
              <h2>{goal.title}</h2>
              <p>{goal.description}</p>
            </div>
            <button>Delete</button>
          </article>
        </li>
      ))}
    </ul>
  );
};

export default CourseGoals;
```

## React UseState

useState is a generic function which takes type of the state as generic argument

```tsx
import Header from "./components/Header";
import goalImg from "./assets/goals.jpg";
import { CourseGoals, type Goal } from "./components/CourseGoals";
import { useState } from "react";

export default function App() {
  const [goals, setGoals] = useState<Goal[]>([
    {
      id: 1,
      title: "Learn TS",
      description: "Learn typescript from the ground up.",
    },
    {
      id: 2,
      title: "Practice TS",
      description: "Practice working with typescript",
    },
  ]);

  return (
    <main>
      <Header image={{ src: goalImg, alt: "list of goals" }}>
        <h1>Your Course Goals</h1>
      </Header>
      <CourseGoals goals={goals} />
    </main>
  );
}
```

## React UseRef

useRef allows access to an HTML element. useRef is a generic function whose generic argument is the type of HTML element which we want this ref to be connected to. useRef needs an initial value which we can set to null because at rendering, the ref is not available yet.

Note that here, the form onSubmit listener is triggered by the button in the form.

```tsx
import { useRef, type FormEvent } from "react";
import { type Goal } from "./CourseGoals";

export type NewGoalProps = {
  addGoal: (newGoal: Goal) => void;
  newId: number;
};

export function NewGoal({ addGoal, newId }: NewGoalProps) {
  const goalRef = useRef<HTMLInputElement>(null);
  const summaryRef = useRef<HTMLInputElement>(null);

  const handleSubmit = function (event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const goalTitle = goalRef.current.value;
    const goalSummary = summaryRef.current.value;
    addGoal({ id: newId, title: goalTitle, description: goalSummary });
  };

  return (
    <form onSubmit={handleSubmit}>
      <p>
        <label htmlFor="goal">Your goal</label>
        <input ref={goalRef} id="goal" type="text" />
      </p>
      <p>
        <label htmlFor="summary">Short summary</label>
        <input ref={summaryRef} id="summary" type="text" />
      </p>
      <p>
        <button>Add Goal</button>
      </p>
    </form>
  );
}
```

# NodeJs and Typescript

## Initializing the project

In an empty folder, execute the following. \-y initialize a default setup. This will create an empty project. The “type” in package.json, is “jscommon” but should be “module”

```
npm init -y
```

Then execute the following. It will add a development dependency toward typescript. \--save-dev indicates that this dependencies should not be installed in production, because the compiled code will be used in production.

```
npm install typescript --save-dev
```

The script in package.json should be the following. This will make sure we have a compile command and a starting command

```json
"scripts": {
  "compile": "tsc",
  "start": "node dist/app.js"
}
```

The tsconfig.json file should be:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "module": "NodeNext",
    "outDir": "dist",
    "lib": ["ES2022", "dom"],
    "strict": true
  }
}
```

Now we can run the following and it will run the app:

```
npm run compile
npm run start
```

## Making a basic server

We have to install the types of node js.

```
npm install --save-dev @types/node
```

Moreover, we have to add the “types”:\[“nodes”\] to the tsconfig.json “compilerOptions”. The following [app.ts](http://app.ts) then creates a server which is accessible at [http\://localhost:3000/](http://localhost:3000/). When accessing it, we understand that this is a GET method and it displays the html.

```ts
import { createServer } from "node:http";

const server = createServer((req, res) => {
  console.log(req.method);
  res.end("<h1>hello</h1>");
});

server.listen(3000);
```

## Adding endpoints

There is a library to create endpoints: Express.

```
npm install express --save
npm install --save-dev @types/express
```

The following code makes a GET [http\://localhost:3000/hello](http://localhost:3000/hello/) endpoint, returning always { message: "hello" }.

```ts
import express from "express";

const app = express();

app.get("/hello", (req, res) => {
  res.json({ message: "hello" });
});

app.listen(3000);
```

Alternatively, we can the express.Router(). The following makes some endpoints. It is important to register the router (with **app.use(router)**) after the json parser (with **app.use(express.json())**). We can add an exception filter middleware which will caught any error of a certain type and return a specific code.

```ts
import express from "express";
import router from "./routes/todo.js";

const app = express();

// register parsing of json request
app.use(express.json());

// register endpoints
app.use(router);

// adding exception filter middleware
app.use(
  (err: Error, request: Request, response: Response, next: NextFunction) => {
    response.status(404).json({ error: err.message });
  }
);

app.listen(3000);
```

```ts
import express from "express";
import { addTodo, getTodos, getTodo, updateTodo, removeTodo } from "../data.js";

const router = express.Router();

router.post("/todos", (request, response) => {
  const text = request.body.text;
  const addedTodo = addTodo(text);
  response.json({ message: "Todo added", todo: addedTodo });
});

router.get("/todos", (request, response) => {
  const all = getTodos();
  response.json({ todos: all });
});

router.get("/todos/:id", (request, response) => {
  const todo = getTodo(+request.params.id);
  response.json(todo);
});

router.patch("/todos/:id", (request, response) => {
  const todo = updateTodo(+request.params.id, request.body.text);
  response.json(todo);
});

router.delete("/todos/:id", (request, response) => {
  removeTodo(+request.params.id);
  response.json({ message: "todo deleted" });
});

export default router;
```

## Testing the Server

By installing the VS code extension REST Client, you can make http files which can be used to make a request. For instance, a POST and GET request:

```http
GET http://localhost:3000/todos
```

```http
POST http://localhost:3000/todos
Content-Type: application/json

{ "text":"faire l'amour à Chloé" }
```

```http
DELETE http://localhost:3000/todos/0.0904760362182172
```

## Running typescript code with Node js

TS is usually transpiled to JS so a browser or node js can run it. NodeJs allows to run directly TS with the following command

```
node app.ts
```

To allow that:

- every type import should be preceded by the type keyword
- every import should import from ts files and not js file

```ts
import express, {
  type NextFunction,
  type Request,
  type Response,
} from "express";
import router from "./routes/todo.ts";
```

- in tsconfig, we have to tell TS that it can import ts files (allowImportingTsExtensions), and that it should not be compiled (noEmit). verbatimModuleSyntax is there to warn non-preceeded-with-type type imports.

```json
{
  "compilerOptions": {
    "allowImportingTsExtensions": true,
    "noEmit": true,
    "verbatimModuleSyntax": true
  }
}
```

not all TS features are supported by this Nodejs feature. Only the TS features that can be only strip out, are supported (hence the name of this NodeJs feature “strip-only mode”). For instance enum is not supported. using the following experimental command will make sure to transform the ts-specific feature to js.

```
node --experimental-transform-types app.ts
```

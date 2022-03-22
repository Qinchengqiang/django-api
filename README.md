# django-api

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

#### django graphql api

## Details

- expose a GraphQL endpoint at `/graphql`.
- The GraphQL schema should consist of a single query, person, which must return a `Person` object.
- A Person object should have the following fields: `email (string)`, `name (string)`, `address (Address)`.
- An Address object should have the following fields: `number (integer)`, `street (string)`, `city (string)`, `state (GraphQL enum)`.


The following query will be used to validate your implementation:
```
query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```


## Table of Contents

- [Install](#install)
- [API](#api)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Install

commands:
```
$ mkdir myApi

$ cd myApi




                                       
$ yarn start
```
the client will run at http://localhost:3000/

## API

## Github

## Maintainers

[@Steven](https://github.com/Qinchengqiang)

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2022 Steven Qin

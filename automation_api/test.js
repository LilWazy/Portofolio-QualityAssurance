const domain = require("supertest")("http://....");
const expect = require("chai").expect;

describe("Scenario Login Feature", function () {
  it("Verify Success Login with registered email and valid password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....@gmail.com", password: "...." });

    expect(response.body.status).to.eql('SUCCESS_LOGIN');
    expect(response.body.data).to.eql('....');
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status", "credentials"); 
  });

  it("Verify Failed Login with registered email and blank password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....@gmail.com", password: "" });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql('....');
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with blank email and valid password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....", password: "...." });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql('....');
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with unregistered email and invalid password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....@gmail.com", password: "...." });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql("....");
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with registered email and invalid password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....@gmail.com", password: "...." });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql("....");
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with blank email and blank password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....", password: ".... });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql('....');
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with max char email and valid password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....@gmail.com", password: "...." });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql('....');
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with registered email and max char password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....@gmail.com", password: "...." });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql('....');
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with max char email and max char password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "....@gmail.com", password: "...." });

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.data).to.eql('....');
    expect(response.body.message).to.eql('....');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

});


import { useNavigate } from 'react-router-dom';

import { useAuth } from '../features/auth/AuthContext';


const LoginPage = () => {

  const { login } = useAuth();

  const navigate = useNavigate();

  const handleDemoLogin = () => {

    login();

    navigate('/');
  };

  const handleOAuthLogin = (
    provider
  ) => {

    window.location.href =
      `/api/auth/${provider}/`;
  };

  return (

    <div className="container">

      <div
        style={{
          textAlign: 'center'
        }}
      >

        <h1>
          InsightFlow
        </h1>

        <p>
          Multi-Tenant Analytics Platform
        </p>

        <br />

        <button
          className="login-btn"
          onClick={handleDemoLogin}
        >
          Login Demo User
        </button>

        <br />
        <br />

        <button
          className="oauth-btn"
          onClick={() =>
            handleOAuthLogin('google')
          }
        >
          Continue with Google
        </button>

        <br />
        <br />

        <button
          className="oauth-btn"
          onClick={() =>
            handleOAuthLogin('github')
          }
        >
          Continue with GitHub
        </button>

      </div>

    </div>
  );
};
export default LoginPage;

import pytest
from unittest.mock import patch, MagicMock
from handler import verify_example_com, handler


class TestVerifyExampleCom:
    """Tests for verify_example_com function."""
    
    @patch('handler.requests.get')
    def test_verify_example_com_success(self, mock_get):
        """Test that verify_example_com succeeds with a 200 response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        response = verify_example_com()
        
        assert response.status_code == 200
        mock_get.assert_called_once_with('https://example.com')
    
    @patch('handler.requests.get')
    def test_verify_example_com_failure(self, mock_get):
        """Test that verify_example_com raises AssertionError on non-200 response."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        with pytest.raises(AssertionError, match="Expected 200, got 404"):
            verify_example_com()


class TestHandler:
    """Tests for the Lambda handler function."""
    
    @patch('handler.requests.get')
    def test_handler_success(self, mock_get):
        """Test that handler succeeds when verify_example_com passes."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        event = {'test': 'data'}
        result = handler(event, None)
        
        assert result == event
    
    @patch('handler.requests.get')
    def test_handler_failure(self, mock_get):
        """Test that handler fails when verify_example_com fails."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        event = {'test': 'data'}
        
        with pytest.raises(AssertionError):
            handler(event, None)


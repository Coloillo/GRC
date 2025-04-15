import api from './api';

/**
 * Risk service for handling risk assessment API calls
 */
const riskService = {
  /**
   * Get all risks
   * @returns {Promise} Promise with risk data
   */
  getRisks: async () => {
    try {
      const response = await api.get('/risk/risks/');
      return response.data;
    } catch (error) {
      console.error('Error fetching risks:', error);
      throw error;
    }
  },

  /**
   * Get risk by ID
   * @param {number} id - Risk ID
   * @returns {Promise} Promise with risk data
   */
  getRiskById: async (id) => {
    try {
      const response = await api.get(`/risk/risks/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching risk with ID ${id}:`, error);
      throw error;
    }
  },

  /**
   * Create a new risk
   * @param {Object} riskData - Risk data
   * @returns {Promise} Promise with the created risk
   */
  createRisk: async (riskData) => {
    try {
      const response = await api.post('/risk/risks/', riskData);
      return response.data;
    } catch (error) {
      console.error('Error creating risk:', error);
      throw error;
    }
  },

  /**
   * Update an existing risk
   * @param {number} id - Risk ID
   * @param {Object} riskData - Updated risk data
   * @returns {Promise} Promise with the updated risk
   */
  updateRisk: async (id, riskData) => {
    try {
      const response = await api.put(`/risk/risks/${id}/`, riskData);
      return response.data;
    } catch (error) {
      console.error(`Error updating risk with ID ${id}:`, error);
      throw error;
    }
  },

  /**
   * Delete a risk
   * @param {number} id - Risk ID
   * @returns {Promise} Promise with the result
   */
  deleteRisk: async (id) => {
    try {
      const response = await api.delete(`/risk/risks/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`Error deleting risk with ID ${id}:`, error);
      throw error;
    }
  },

  /**
   * Get risk metrics summary
   * @returns {Promise} Promise with risk metrics data
   */
  getRiskMetrics: async () => {
    try {
      const response = await api.get('/risk/risks/metrics/');
      return response.data;
    } catch (error) {
      console.error('Error fetching risk metrics:', error);
      throw error;
    }
  },

  /**
   * Get treatment by ID
   * @param {number} riskId - Risk ID
   * @param {number} treatmentId - Treatment ID
   * @returns {Promise} Promise with treatment data
   */
  getTreatmentById: async (riskId, treatmentId) => {
    try {
      const response = await api.get(`/risk/risks/${riskId}/treatments/${treatmentId}/`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching treatment with ID ${treatmentId}:`, error);
      throw error;
    }
  },

  /**
   * Create a new treatment
   * @param {number} riskId - Risk ID
   * @param {Object} treatmentData - Treatment data
   * @returns {Promise} Promise with the created treatment
   */
  createTreatment: async (riskId, treatmentData) => {
    try {
      const response = await api.post(`/risk/risks/${riskId}/treatments/`, treatmentData);
      return response.data;
    } catch (error) {
      console.error('Error creating treatment:', error);
      throw error;
    }
  },

  /**
   * Update an existing treatment
   * @param {number} riskId - Risk ID
   * @param {number} treatmentId - Treatment ID
   * @param {Object} treatmentData - Updated treatment data
   * @returns {Promise} Promise with the updated treatment
   */
  updateTreatment: async (riskId, treatmentId, treatmentData) => {
    try {
      const response = await api.put(`/risk/risks/${riskId}/treatments/${treatmentId}/`, treatmentData);
      return response.data;
    } catch (error) {
      console.error(`Error updating treatment with ID ${treatmentId}:`, error);
      throw error;
    }
  },

  /**
   * Delete a treatment
   * @param {number} riskId - Risk ID
   * @param {number} treatmentId - Treatment ID
   * @returns {Promise} Promise with the result
   */
  deleteTreatment: async (riskId, treatmentId) => {
    try {
      const response = await api.delete(`/risk/risks/${riskId}/treatments/${treatmentId}/`);
      return response.data;
    } catch (error) {
      console.error(`Error deleting treatment with ID ${treatmentId}:`, error);
      throw error;
    }
  }
};

export default riskService; 
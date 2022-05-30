export function useFormatter() {
  function formatDate(date) {
    return new Date(date).toLocaleDateString('en-us', {
      weekday: 'long',
      month: 'long',
      day: 'numeric',
      year: 'numeric',
    });
  };

  return {
    formatDate,
  };
}

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        formatted_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = ''.join(local_name.split('+')[0].split('.'))
            formatted_emails.add((local_name, domain_name))
        return len(formatted_emails)

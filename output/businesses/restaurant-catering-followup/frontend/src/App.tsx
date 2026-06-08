import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import EventInquiryDemo from './views/EventInquiryDemo';
import CateringRevenueCalculator from './views/CateringRevenueCalculator';
import InboxAuditForm from './views/InboxAuditForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'event-inquiry-demo': EventInquiryDemo,
  'catering-revenue-calculator': CateringRevenueCalculator,
  'inbox-audit-form': InboxAuditForm,
  'pilot-signup': PilotSignup,
    };

    export default function App() {
      const [route, setRoute] = useState<keyof typeof routes>('landing');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className="app-shell">
          <nav className="top-nav">
            <strong>{businessMeta.name}</strong>
              <button onClick={() => setRoute('landing')} className={route === 'landing' ? 'active' : ''}>Landing</button>
          <button onClick={() => setRoute('event-inquiry-demo')} className={route === 'event-inquiry-demo' ? 'active' : ''}>EventInquiryDemo</button>
          <button onClick={() => setRoute('catering-revenue-calculator')} className={route === 'catering-revenue-calculator' ? 'active' : ''}>CateringRevenueCalculator</button>
          <button onClick={() => setRoute('inbox-audit-form')} className={route === 'inbox-audit-form' ? 'active' : ''}>InboxAuditForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }

import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import ReportBeforeAfter from './views/ReportBeforeAfter';
import ClientProofDemo from './views/ClientProofDemo';
import StackAuditForm from './views/StackAuditForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'report-before-after': ReportBeforeAfter,
  'client-proof-demo': ClientProofDemo,
  'stack-audit-form': StackAuditForm,
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
          <button onClick={() => setRoute('report-before-after')} className={route === 'report-before-after' ? 'active' : ''}>ReportBeforeAfter</button>
          <button onClick={() => setRoute('client-proof-demo')} className={route === 'client-proof-demo' ? 'active' : ''}>ClientProofDemo</button>
          <button onClick={() => setRoute('stack-audit-form')} className={route === 'stack-audit-form' ? 'active' : ''}>StackAuditForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }
